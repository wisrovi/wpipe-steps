#!/usr/bin/env python
"""
Simple fix: Remove self._pipeline = None and replace self._pipeline with pipe
"""
import re
import os
import glob

def fix_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    original = content
    
    # Remove self._pipeline = None
    content = re.sub(r'\s*self\._pipeline = None\s*\n', '\n', content)
    
    # Replace self._pipeline references with local pipe
    # In execute method, change self._pipeline to pipe
    lines = content.split('\n')
    new_lines = []
    in_execute = False
    execute_indent = ''
    
    for i, line in enumerate(lines):
        # Detect execute method
        if 'def execute(' in line:
            in_execute = True
            execute_indent = line[:len(line) - len(line.lstrip())]
            new_lines.append(line)
            continue
        
        # Detect end of execute method
        if in_execute and line.strip() and not line.startswith(execute_indent + '    '):
            in_execute = False
        
        # In execute, replace self._pipeline with pipe
        if in_execute:
            new_line = line.replace('self._pipeline', 'pipe')
            new_lines.append(new_line)
        else:
            new_lines.append(line)
    
    content = '\n'.join(new_lines)
    
    if content != original:
        with open(filepath, 'w') as f:
            f.write(content)
        return True
    return False

# Run
base_dir = '/home/william.rodriguez/Documents/wpipe-steps/wpipe_steps/huggingface'
files = glob.glob(f'{base_dir}/**/*.py', recursive=True)
fixed = 0
for filepath in files:
    if '__init__.py' in filepath:
        continue
    if fix_file(filepath):
        print(f'Fixed: {filepath}')
        fixed += 1

print(f'\nFixed {fixed} files')
