k, n = map(int, input().split())

a = list(map(int, input().split()))

ans = 0
for i in a:
    ans = ans + 1 if i >= a[n - 1] and i > 0 else ans
print(ans)

