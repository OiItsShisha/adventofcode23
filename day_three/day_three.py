from pathlib import Path
from itertools import permutations
with open(Path("./d3data.txt"), encoding='utf8') as f: data = f.readlines()
l = []
[l.append(list(line.strip())) for line in data]
row = 0
total = 0
for line in l:
    f, num_string, col= False, "", 0
    for char in line:
        if char.isnumeric():
            num_string+=char
            col_back, col_front, row_back, row_front = col-1, col+1, row-1, row+1
            perms = set(permutations([row_back, row, row_front, col_back, col, col_front ],2))
            perms = [x for x in perms if x[0] >=0 and x[1] >= 0]
            perms = [x for x in perms if col_back <= x[1] <= col_front and row_back <= x[0] <= row_front]
            perms = [x for x in perms if x != (row, col)]
            perms = [x for x in perms if x[0] < len(l) and x[1] < len(line)]
            for i in perms:
                if l[i[0]][i[1]] == ".":
                    continue
                elif l[i[0]][i[1]].isnumeric():
                    continue
                else:
                    f = True
            if col == len(line)-1 and f: total+=int(num_string); num_string=""; f=False
        elif char == "." and not f: num_string=""
        else: 
            if f: total+=int(num_string); num_string=""; f=False
        col += 1
    row += 1
print(total)

row = 0
total = 0
for line in l:
    f, num_string, col= False, "", 0
    for char in line:
        if char.isnumeric():
            num_string+=char
            col_back, col_front, row_back, row_front = col-1, col+1, row-1, row+1
            perms = set(permutations([row_back, row, row_front, col_back, col, col_front ],2))
            perms = [x for x in perms if x[0] >=0 and x[1] >= 0]
            perms = [x for x in perms if col_back <= x[1] <= col_front and row_back <= x[0] <= row_front]
            perms = [x for x in perms if x != (row, col)]
            perms = [x for x in perms if x[0] < len(l) and x[1] < len(line)]
            for i in perms:
                if l[i[0]][i[1]] == ".":
                    continue
                elif l[i[0]][i[1]].isnumeric():
                    continue
                elif l[i[0][i[1]]] == '*':
                    f = True
            if col == len(line)-1 and f: total+=int(num_string); num_string=""; f=False
        elif char == "." and not f: num_string=""
        else: 
            if f: total+=int(num_string); num_string=""; f=False
        col += 1
    row += 1