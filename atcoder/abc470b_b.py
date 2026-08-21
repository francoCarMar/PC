n = int(input())

arr = map(int, input().split())

d = {}
rep_max = 0
for i in arr:
    d[i] = d.get(i, 0) + 1
    rep_max = max(d[i], rep_max)

print(n - rep_max)


