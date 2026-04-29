#!/usr/bin/env python
"""
Fix HuggingFace step files to properly implement BaseStep.
Pattern:
1. Keep __init__ as is
2. Rename __call__ to _execute_impl and keep @to_obj
3. Add execute() method that calls _execute_impl()
"""
import re
import os
import glob

def fix_step_file(filepath):
    """Fix a single step file."""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Skip if already fixed (has execute method that calls _execute_impl)
    if 'def execute(' in content and '_execute_impl' in content:
        print(f"  Already fixed: {filepath}")
        return False
    
    # Find __call__ method with @to_obj
    # Pattern: @to_obj\n    def __call__(self, ...):\n        ...
    pattern = r'(@to_obj\s*\n\s*def\s+)__call__(\s*\(self[^)]*\)[^:]*:.*?)(?=\n    def\s+|\n\Z)'
    
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        print(f"  WARNING: Could not find __call__ in {filepath}")
        return False
    
    # Get the full __call__ method
    # We need to find the complete method including body
    lines = content.split('\n')
    in_call = False
    call_start = -1
    call_end = -1
    indent_level = 0
    
    for i, line in enumerate(lines):
        if '@to_obj' in line and i < len(lines) - 1 and 'def __call__' in lines[i+1]:
            in_call = True
            call_start = i
        elif in_call:
            if line.strip() and not line.startswith('    '):  # Method ended
                call_end = i
                break
    
    if call_start == -1:
        print(f"  WARNING: Could not parse __call__ in {filepath}")
        return False
    
    if call_end == -1:
        call_end = len(lines)
    
    # Extract the __call__ method
    call_lines = lines[call_start:call_end]
    call_text = '\n'.join(call_lines)
    
    # Replace __call__ with _execute_impl
    new_call_text = call_text.replace('def __call__(', 'def _execute_impl(')
    new_call_text = new_call_text.replace('@to_obj', '@to_obj')
    
    # Add execute method
    execute_method = '''
    def execute(self, data):
        """Execute the step - required by BaseStep."""
        return self._execute_impl(data)
'''
    
    # Replace in content
    new_content = content.replace(call_text, new_call_text + execute_method)
    
    with open(filepath, 'w') as f:
        f.write(new_content)
    
    print(f"  Fixed: {filepath}")
    return True

def main():
    base_dir = '/home/william.rodriguez/Documents/wpipe-steps/wpipe_steps/huggingface'
    
    # Find all Python files
    files = glob.glob(f'{base_dir}/**/*.py', recursive=True)
    
    fixed_count = 0
    for filepath in files:
        if '__init__.py' in filepath:
            continue
        print(f"Processing: {filepath}")
        if fix_step_file(filepath):
            fixed_count += 1
    
    print(f"\nFixed {fixed_count} files")

if __name__ == '__main__':
    main()
