import re

file_path = 'blackjack.py'
comment_pattern = re.compile(r'^\s*#')
blank_pattern = re.compile(r'^\s*$')
lines_of_code = 0

with open(file_path, 'r') as file:
    lines = file.readlines()

for line in lines:
    if not comment_pattern.match(line) and not blank_pattern.match(line):
        lines_of_code += 1

print(f"Total lines of code: {lines_of_code}")
