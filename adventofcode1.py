with open("input_advent1.txt", "r") as f:
    values = [line.strip() for line in f if line.strip()]
    
curr = 50
ans = 0
    
for val in values:
    dir = val[0]
    if dir == 'R':
        curr = curr + int(val[1:])
    else:
        curr = curr - int(val[1:])
        
    print(curr)
    if curr%100 == 0:
        ans = ans + 1

print(ans)