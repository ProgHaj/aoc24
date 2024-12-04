from pprint import pprint

with open("input", "r") as f:
    data = f.readlines()
    

data = [[letter for letter in row  if letter != "\n"] for row in data]
word = "XMAS"

pprint(data)

count = 0

def xmas(i, j, pos, path, direction=None):
    global count
    if pos == len(word):
        return
    
    pos_to_check = []
    if direction:
        pos_to_check.append([i + direction[0], j + direction[1]])
    else:
        for a in range(3):
            for b in range(3):
                if a == 1 and b == 1:
                    continue

                pos_to_check.append((i-1+a, j-1+b))
            
    for a,b, in pos_to_check:
        if a < 0 or a >= len(data):
            continue
        
        if b < 0 or b >= len(data[0]):
            continue
        
        if data[a][b] == word[pos]:
            if pos == len(word) - 1:
                count += 1
                res_string = ""
                for q,w in path:
                    res_string += data[q][w]
                res_string += data[a][b]
                print("path", path + [(a,b)], res_string, direction, count)
            
            xmas(a,b, pos + 1, path + [(a,b)],  direction = ((a - i), (b - j)))
            

for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == "X":
            xmas(i,j,1, path=[(i,j)])

print(count)