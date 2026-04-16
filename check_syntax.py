import ast
import sys

try:
    with open('core/models.py', 'r') as f:
        code = f.read()
        ast.parse(code)
    print("No syntax errors")
except SyntaxError as e:
    print(f"Line {e.lineno}: {e.msg}")
    if e.text:
        print(f"Text: {e.text.strip()}")
    sys.exit(1)
