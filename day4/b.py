from pprint import pprint

with open("input", "r") as f:
    data = f.readlines()
    

data = [[letter for letter in row  if letter != "\n"] for row in data]
word = "MAS"

pprint(data)

res_count = 0

def xmas(i, j, pos, path):
    global res_count
    if pos == len(word):
        return
    
    pos_to_check = [((i-1, j-1), (i + 1, j + 1)), ((i-1, j+1), (i + 1, j - 1))]
    res = []
    
    for a,b, in pos_to_check:
        if a[0] < 0 or b[0] >= len(data):
            continue
        
        if a[1] < 0 or b[1] >= len(data[0]):
            continue

        if b[1] < 0 or a[1] >= len(data[0]):
            continue
        

        x_mas = False
        right_mas = False
        if data[a[0]][a[1]] == "M" and data[b[0]][b[1]] == "S":
            x_mas = True

        if data[a[0]][a[1]] == "S" and data[b[0]][b[1]] == "M":
            x_mas = True
        
        res.append(x_mas)
            
    if sum(res) == 2:
        res_count += 1
            

for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == "A":
            xmas(i,j,1, path=[(i,j)])

print(res_count)