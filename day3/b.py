import re

with open("input", "r") as f:
    text = f.read()

entries = re.findall(r"mul\((\d+),(\d+)\)|(do)\(\)|(don't)\(\)", text)

enabled = True
res = 0
for entry in entries:
    if entry[2]:
        enabled = True
        continue
    if entry[3]:
        enabled = False
        continue
    
    if not enabled:
        continue
    
    res += int(entry[0]) * int(entry[1])
    
print(res)