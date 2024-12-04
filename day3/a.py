import re

with open("input", "r") as f:
    text = f.read()

entries = re.findall(r"mul\((\d+),(\d+)\)", text)
print(entries)
res = 0
for entry in entries:
    res += int(entry[0]) * int(entry[1])

print(res)