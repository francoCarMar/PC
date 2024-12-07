arr = map(str, input().split(","))

ans = 0
for range in arr:
    a,b = range.split("-")
    x = a[:int(len(a)//2)]
    a = int(a)
    b = int(b)
    if x == '':
        x = 0
    x = int(x)
    while True:
        dupli = int(str(x) + str(x))
        if dupli > b: break
        if dupli >= a:
            ans = ans + dupli
        x = x + 1
print(ans)