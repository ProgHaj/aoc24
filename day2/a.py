with open("input", "r") as f:
    data = f.read()

safe = 0
unsafe = 0
rows = data.split("\n")
for row in rows:
    values = row.split()
    
    for i in range(1, len(values) - 1):
        prev = int(values[i-1])
        current = int(values[i])
        next = int(values[i+1])
        
        is_ladder = (prev < current < next) or (prev > current > next) 
        prev_dist = abs(prev - current)
        next_dist = abs(current - next)
        is_prev_adj = prev_dist >= 1 and prev_dist <= 3
        is_next_adj = next_dist >= 1 and next_dist <= 3
        if not (is_ladder and is_prev_adj and is_next_adj):
            unsafe += 1
            break
        
safe = len(rows) - unsafe
print(safe)