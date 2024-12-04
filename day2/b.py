with open("input", "r") as f:
    data = f.read()

def determine_safe(values, ok_remove = 1):
    row_unsafe = -1
    for i in range(len(values)):
        prev = int(values[i-1]) if i > 0 else None
        current = int(values[i])
        next = int(values[i+1]) if i < len(values) - 1 else None
        
        is_ladder = (prev < current < next) or (prev > current > next) 
        is_ladder_0 = (current < next) or (current > next) 
        is_ladder_max = (prev < current) or (prev > current) 
        prev_dist = abs(prev - current)
        next_dist = abs(current - next)
        is_prev_adj = prev_dist >= 1 and prev_dist <= 3
        is_next_adj = next_dist >= 1 and next_dist <= 3
        
        if i == 0:
            if not (is_ladder_0 and is_next_adj):
                row_unsafe = i
                break
        elif i == len(values) - 1:
            if not (is_ladder_max and is_prev_adj):
                row_unsafe = i
                break
        else:
            if not (is_ladder and is_prev_adj and is_next_adj):
                row_unsafe = i
                break
    
    if row_unsafe != -1:
        if ok_remove != 0:
            for i in range(len(values)):
                tmp_values = values[0:i] + values[i+1:len(values)]
                safe = determine_safe(values=tmp_values, ok_remove=ok_remove - 1)
                if safe:
                    return safe
        
        return 0

    
    return 1
        
reports = []
rows = data.split("\n")
for row in rows:
    values = row.split()
    safe = determine_safe(values)
    reports.append(safe)
        
print(sum(reports))