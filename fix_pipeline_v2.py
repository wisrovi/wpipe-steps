#!/usr/bin/env python
"""
Fix all HuggingFace steps to use the proven working pattern.
Pattern from classification.py which works:
- No self._pipeline stored
- Create pipeline fresh in execute()
- Handle both dict and SimpleNamespace
"""
import re
import os
import glob

def fix_file(filepath):
    """Fix a single step file to match working pattern."""
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    # Check if file needs fixing
    content = ''.join(lines)
    if 'self._pipeline' not in content and 'from transformers import pipeline' in content:
        return False  # Already fixed
    
    new_lines = []
    in_init = False
    in_execute = False
    init_indent = ''
    execute_indent = ''
    pipeline_created = False
    skip_lines = 0
    
    for i, line in enumerate(lines):
        if skip_lines > 0:
            skip_lines -= 1
            continue
            
        # Detect __init__ method
        if 'def __init__(' in line:
            in_init = True
            in_execute = False
            init_indent = line[:len(line) - len(line.lstrip())]
            new_lines.append(line)
            continue
            
        # Detect execute method
        if 'def execute(' in line:
            in_init = False
            in_execute = True
            execute_indent = line[:len(line) - len(line.lstrip())]
            new_lines.append(line)
            pipeline_created = False
            continue
            
        # Remove self._pipeline = None from __init__
        if in_init and 'self._pipeline = None' in line:
            continue  # Skip this line
            
        # Handle _pipeline usage in execute
        if in_execute and 'self._pipeline' in line:
            # Replace with local pipe variable
            indent = line[:len(line) - len(line.lstrip())]
            if 'self._pipeline = None' in line:
                continue  # Skip
            elif 'if self._pipeline is None:' in line:
                # Replace with pipeline creation block
                new_lines.append(indent + 'from transformers import pipeline\n')
                new_lines.append(indent + 'try:\n')
                new_lines.append(indent + '    # Try local files first\n')
                # We need to know the task - extract from original line
                new_lines.append(indent + '    pipe = pipeline(\n')
                skip_lines = 0
                continue
            elif 'self._pipeline = pipeline(' in line:
                # This is the pipeline creation - skip original
                continue
            elif 'self._pipeline(' in line:
                # Calling the pipeline - replace with pipe
                new_line = line.replace('self._pipeline', 'pipe')
                new_lines.append(new_line)
                continue
                
        # Add pipeline creation after "from transformers import pipeline"
        if in_execute and 'from transformers import pipeline' in line and not pipeline_created:
            new_lines.append(line)
            indent = line[:len(line) - len(line.lstrip())]
            new_lines.append(indent + 'try:\n')
            new_lines.append(indent + '    # Try local files first\n')
            new_lines.append(indent + '    pipe = pipeline(\n')
            new_lines.append(indent + '        task="...",  # TODO: keep original task\n')
            new_lines.append(indent + '        model=self.model_name,\n')
            new_lines.append(indent + '        device=self.device,\n')
            new_lines.append(indent + '        local_files_only=True,\n')
            new_lines.append(indent + '    )\n')
            new_lines.append(indent + 'except Exception:\n')
            new_lines.append(indent + '    print(f"Downloading model {self.model_name} (first time)...")\n')
            new_lines.append(indent + '    pipe = pipeline(\n')
            new_lines.append(indent + '        task="...",  # TODO: keep original task\n')
            new_lines.append(indent + '        model=self.model_name,\n')
            new_lines.append(indent + '        device=self.device,\n')
            new_lines.append(indent + '        local_files_only=False,\n')
            new_lines.append(indent + '    )\n')
            pipeline_created = True
            continue
            
        new_lines.append(line)
    
    # Write back
    with open(filepath, 'w') as f:
        f.writelines(new_lines)
    
    return True

def main():
    base_dir = '/home/william.rodriguez/Documents/wpipe-steps/wpipe_steps/huggingface'
    files = glob.glob(f'{base_dir}/**/*.py', recursive=True)
    
    fixed = 0
    for filepath in files:
        if '__init__.py' in filepath:
            continue
        print(f'Processing: {filepath}')
        if fix_file(filepath):
            print(f'  Fixed: {filepath}')
            fixed += 1
    
    print(f'\nFixed {fixed} files')

if __name__ == '__main__':
    main()
