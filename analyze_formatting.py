import re

with open('C:\Users\tony.dunsworth\projects\attitude_adjustment\Akimitsu_Takeuchi_Research_Document.md', 'r') as f:
    content = f.read()

print(f"Initial escaped newlines in '\\\\\\\\n   ': {content.count('\\\\\\\\n   ')}")
print(f"Initial escaped newlines in '\\\\\\\\n    ': {content.count('\\\\\\\\n    ')}")
print(f"Initial escaped newlines in '\\\\\\\\\\\\\\\\n\\\\\\\\\\\\\\\\n': {content.count('\\\\\\\\\\\\n\\\\\\\\\\\\n')}")

pattern1 = re.compile(r'\\\\\\\\n   ')
pattern2 = re.compile(r'\\\\\\\\n    ')
pattern3 = re.compile(r'\\\\\\\\n\\\\\\\\n')

print(f"Pattern 1 matches: {len(pattern1.findall(content))}")
print(f"Pattern 2 matches: {len(pattern2.findall(content))}")
print(f"Pattern 3 matches: {len(pattern3.findall(content))}")

with open('C:\Users\tony.dunsworth\projects\attitude_adjustment\Akimitsu_Takeuchi_Research_Document.md', 'rb') as f:
    binary_content = f.read()
    
print("\nLooking for octal\\x5c\\x6e patterns:")
octal_matches = re.findall(b'\\x5c\\x6e   ', binary_content)
print(f"Found {len(octal_matches)} instances of '\\\\\\\\n   '")

octal_matches = re.findall(b'\\x5c\\x6e    ', binary_content)
print(f"Found {len(octal_matches)} instances of '\\\\\\\\n    '")

with open('C:\Users\tony.dunsworth\projects\attitude_adjustment\Akimitsu_Takeuchi_Research_Document.md', 'r', newline='') as f:
    universal_content = f.read()
    
print(f"\nTotal newlines in universal reading: {universal_content.count('\\n')}")
print(f"First 200 chars: {universal_content[:200]}")