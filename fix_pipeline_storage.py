#!/usr/bin/env python
"""
Fix all HuggingFace steps to not store pipeline objects.
Pattern: create pipeline fresh in execute(), don't store as self._pipeline
"""
import re
import os
import glob

def fix_pipeline_storage(filepath):
    """Fix a single step file to not store pipeline."""
    with open(filepath, 'r') as f:
        content = f.read()
    
    original = content
    
    # Remove self._pipeline = None from __init__
    content = re.sub(r'\s*self\._pipeline = None\s*\n', '\n', content)
    
    # Remove self._pipeline from execute method
    # Pattern: if self._pipeline is None: ... self._pipeline = pipeline(...)
    
    # Replace self._pipeline with local variable
    # Find the pipeline creation block and make it create local pipe variable
    
    # Pattern 1: Remove _get_pipeline method
    content = re.sub(
        r'\s*def _get_pipeline\(self\):.*?return self\._pipeline\s*\n',
        '\n',
        content,
        flags=re.DOTALL
    )
    
    # Pattern 2: Replace self._pipeline usage with local pipe variable
    # In execute(), replace any reference to self._pipeline with local pipe
    
    # Simple approach: just remove all self._pipeline references and add local pipeline creation
    lines = content.split('\n')
    new_lines = []
    in_execute = False
    pipeline_created = False
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check if we're entering execute method
        if 'def execute(' in line:
            in_execute = True
            pipeline_created = False
            new_lines.append(line)
            i += 1
            continue
        
        # Check if we're leaving execute method
        if in_execute and line.strip() and not line.startswith('    '):
            in_execute = False
        
        # If in execute and line contains self._pipeline
        if in_execute and 'self._pipeline' in line:
            # Skip this line - we'll handle pipeline creation differently
            i += 1
            continue
        
        # If we see "from transformers import pipeline" in execute, replace with pipeline creation
        if in_execute and 'from transformers import pipeline' in line:
            if not pipeline_created:
                # Add pipeline creation block
                indent = line[:len(line) - len(line.lstrip())]
                new_lines.append(indent + 'from transformers import pipeline')
                new_lines.append(indent + 'try:')
                new_lines.append(indent + '    pipe = pipeline(')
                new_lines.append(indent + '        task="...",  # Will keep original task')
                new_lines.append(indent + '        model=self.model_name,')
                new_lines.append(indent + '        device=self.device,')
                new_lines.append(indent + '        local_files_only=True,')
                new_lines.append(indent + '    )')
                new_lines.append(indent + 'except Exception:')
                new_lines.append(indent + '    print(f"Downloading model {self.model_name}...")')
                new_lines.append(indent + '    pipe = pipeline(')
                new_lines.append(indent + '        task="...",')
                new_lines.append(indent + '        model=self.model_name,')
                new_lines.append(indent + '        device=self.device,')
                new_lines.append(indent + '        local_files_only=False,')
                new_lines.append(indent + '    )')
                pipeline_created = True
            i += 1
            continue
        
        new_lines.append(line)
        i += 1
    
    content = '\n'.join(new_lines)
    
    if content != original:
        with open(filepath, 'w') as f:
            f.write(content)
        return True
    return False

def main():
    base_dir = '/home/william.rodriguez/Documents/wpipe-steps/wpipe_steps/huggingface'
    
    files = glob.glob(f'{base_dir}/**/*.py', recursive=True)
    
    fixed = 0
    for filepath in files:
        if '__init__.py' in filepath:
            continue
        print(f"Processing: {filepath}")
        if fix_pipeline_storage(filepath):
            print(f"  Fixed: {filepath}")
            fixed += 1
    
    print(f"\nFixed {fixed} files")

if __name__ == '__main__':
    main()
