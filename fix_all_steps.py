#!/usr/bin/env python
"""
Master fix for all HuggingFace steps.
Uses the proven working pattern from classification.py
"""
import os
import re

def fix_step_file(filepath):
    """Fix a step file to match the working pattern."""
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    # Find key sections
    init_start = -1
    execute_start = -1
    
    for i, line in enumerate(lines):
        if 'def __init__(' in line:
            init_start = i
        elif 'def execute(' in line:
            execute_start = i
            break
    
    if init_start == -1 or execute_start == -1:
        print(f"  WARNING: Could not find sections in {filepath}")
        return False
    
    # Build new file
    new_lines = []
    
    # 1. Add imports (ensure correct imports)
    for i in range(init_start):
        line = lines[i]
        # Fix imports
        if 'from wpipe import' in line:
            continue  # Skip wpipe imports
        if 'from wpipe_steps.core.base import BaseStep' in line:
            new_lines.append('from typing import Any, Dict, Optional\n')
            new_lines.append('from wpipe_steps.core.base import BaseStep\n')
        else:
            new_lines.append(line)
    
    # 2. Fix __init__ method - remove self._pipeline = None
    i = init_start
    init_indent = lines[i][:len(lines[i]) - len(lines[i].lstrip())]
    
    # Write def __init__ line
    new_lines.append(lines[i])
    i += 1
    
    # Skip until we find the body of __init__
    while i < execute_start:
        line = lines[i]
        
        # Skip self._pipeline = None
        if 'self._pipeline = None' in line:
            i += 1
            continue
            
        # Skip empty lines at end of __init__
        if line.strip() == '' and i > init_start + 5:
            break
            
        new_lines.append(line)
        i += 1
    
    # 3. Fix execute method
    # Find execute method
    while i < len(lines):
        line = lines[i]
        if 'def execute(' in line:
            execute_indent = line[:len(line) - len(line.lstrip())]
            new_lines.append(line)
            i += 1
            break
        i += 1
    
    # Now add the fixed execute method body
    # We'll add: handle input, create pipeline, run inference
    # For now, just copy the rest of the file but fix self._pipeline references
    while i < len(lines):
        line = lines[i]
        
        # Replace self._pipeline with local pipe
        new_line = line.replace('self._pipeline', 'pipe')
        
        # Add pipeline creation if we see "from transformers import pipeline"
        if 'from transformers import pipeline' in line:
            indent = line[:len(line) - len(line.lstrip())]
            new_lines.append(line)
            new_lines.append(indent + 'try:\n')
            new_lines.append(indent + '    # Try local files first\n')
            # The actual pipeline creation will be in the original code
        else:
            new_lines.append(new_line)
            
        i += 1
    
    # Write back
    with open(filepath, 'w') as f:
        f.writelines(new_lines)
    
    return True

def main():
    base_dir = '/home/william.rodriguez/Documents/wpipe-steps/wpipe_steps/huggingface'
    
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.py') and file != '__init__.py':
                filepath = os.path.join(root, file)
                print(f"Processing: {filepath}")
                if fix_step_file(filepath):
                    print(f"  Fixed: {filepath}")

if __name__ == '__main__':
    main()
