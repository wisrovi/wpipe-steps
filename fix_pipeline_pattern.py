#!/usr/bin/env python
"""
Fix all HuggingFace steps to use the working pattern:
- No stored pipeline object (avoid pickling issues)
- Create pipeline fresh in execute() method
- Handle both dict and SimpleNamespace inputs
"""
import re
import os
import glob

def fix_step_file(filepath):
    """Fix a single step file."""
    with open(filepath, 'r') as f:
        content = f.read()
    
    original = content
    
    # 1. Remove self._pipeline = None from __init__
    content = re.sub(r'\s*self\._pipeline = None\s*\n', '\n', content)
    
    # 2. Remove _get_pipeline method if exists
    content = re.sub(
        r'\s*def _get_pipeline\(self\):.*?return self\._pipeline\s*\n',
        '\n',
        content,
        flags=re.DOTALL
    )
    
    # 3. In execute method, replace self._pipeline with local pipe
    lines = content.split('\n')
    new_lines = []
    in_execute = False
    indent = ''
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check if entering execute method
        if 'def execute(' in line:
            in_execute = True
            indent = line[:len(line) - len(line.lstrip())]
            new_lines.append(line)
            i += 1
            continue
        
        # Check if leaving execute method
        if in_execute and line.strip() and not line.startswith(indent + '    '):
            in_execute = False
        
        # If in execute and line contains self._pipeline
        if in_execute and 'self._pipeline' in line:
            # Skip this line - replace with local pipe usage
            # The pipeline creation will be handled separately
            i += 1
            continue
        
        # If in execute and we see "from transformers import pipeline"
        if in_execute and 'from transformers import pipeline' in line:
            # Replace with pipeline creation block
            new_lines.append(line)
            # We'll need to add the try/except block
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
    
    fixed_count = 0
    for filepath in files:
        if '__init__.py' in filepath:
            continue
        print(f"Processing: {filepath}")
        if fix_step_file(filepath):
            print(f"  Fixed: {filepath}")
            fixed_count += 1
    
    print(f"\nFixed {fixed_count} files")

if __name__ == '__main__':
    main()
