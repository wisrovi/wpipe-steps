#!/usr/bin/env python
"""
Fix all HuggingFace steps to not use @to_obj and not store pipeline object.
Pattern matching classification.py fix.
"""
import re
import os
import glob

def fix_step_file(filepath):
    """Fix a single step file to match working classification.py pattern."""
    with open(filepath, 'r') as f:
        content = f.read()
    
    original = content
    
    # 1. Remove 'from wpipe import to_obj' line
    content = re.sub(r'\nfrom wpipe import to_obj\s*\n', '\n', content)
    
    # 2. Remove @to_obj decorator before _execute_impl
    content = re.sub(r'\n\s*@to_obj\s*\n', '\n', content)
    
    # 3. Remove 'execute' method that calls _execute_impl
    # Pattern: def execute(...):\n        """...""\n        return self._execute_impl(data)
    content = re.sub(
        r'\n\s*def execute\(self.*?\):\s*\n\s*"""[^"]*"""\s*\n\s*return self\._execute_impl\(data\)\s*\n',
        '\n',
        content,
        flags=re.DOTALL
    )
    
    # 4. Rename _execute_impl back to execute (since we don't need the wrapper)
    content = re.sub(r'def _execute_impl\(self', 'def execute(self', content)
    
    # 5. Remove any stored _pipeline instance variable and _get_pipeline method
    # Instead, create pipeline inside execute method
    
    if content != original:
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"  Fixed: {filepath}")
        return True
    else:
        print(f"  No changes: {filepath}")
        return False

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
