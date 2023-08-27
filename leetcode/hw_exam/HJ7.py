# handle input
lst = input().strip().split(";")
x = 0
y = 0
for line in lst:
    line = line.strip()
    if len(line) != 2 and len(line) != 3:
        continue
    if line[0] not in ['A', 'D', 'W', 'S']:
        continue
    if not line[1].isdigit() or int(line[1]) == 0:
        continue
    if len(line) == 3:
        if not line[2].isdigit():
            continue
    # handle current line
    unit = int(line[1:3])
    if line[0] == 'A':
        x -= unit
        continue
    if line[0] == 'D':
        x += unit
        continue
    if line[0] == 'W':
        y += unit
        continue
    if line[0] == 'S':
        y -= unit
        continue

print(str(x)+","+str(y))
