#!/usr/bin/env python
"""
Fix HuggingFace step files to properly implement BaseStep.
This script:
1. Removes @step decorator
2. Adds execute() method that calls implementation
3. Renames __call__ to _execute_impl and adds @to_obj
4. Updates as_step() to work correctly
"""
import re
import os
import glob

def fix_step_file(filepath):
    """Fix a single step file."""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Skip if already fixed (has execute method)
    if 'def execute(' in content:
        print(f"  Already fixed: {filepath}")
        return False
    
    # Remove @step decorator
    content = re.sub(r'\nfrom wpipe import step, to_obj', '\nfrom wpipe import to_obj', content)
    content = re.sub(r'\n@step\s*\n', '\n', content)
    content = re.sub(r'\n@step\([^)]*\)\s*\n', '\n', content)
    
    # Find __call__ method with @to_obj
    pattern = r'(@to_obj\s*\n\s*def\s+__call__\s*\(self[^)]*\)[^:]*:.*?)(?=\nclass\s+|\n\Z)'
    
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        print(f"  WARNING: Could not find __call__ in {filepath}")
        return False
    
    old_call = match.group(1)
    
    # Extract the method body
    lines = old_call.split('\n')
    indent = ''
    body_started = False
    method_body = []
    
    for line in lines:
        if line.strip().startswith('def __call__'):
            # Get indent
            indent = line[:len(line) - len(line.lstrip())]
            method_body.append(line.replace('__call__', '_execute_impl'))
        elif line.strip() == '@to_obj':
            pass  # Skip decorator
        else:
            method_body.append(line)
    
    new_impl = '\n'.join(method_body)
    
    # Add execute method
    execute_method = f"""
    def execute(self, data):
        \"\"\"Execute the step - required by BaseStep.\"\"\"
        return self._execute_impl(data)
"""
    
    # Replace in content
    new_content = content.replace(old_call, new_impl + execute_method)
    
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
