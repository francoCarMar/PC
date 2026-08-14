n = int(input())

ans = 0
for i in range(n):
    a = map(int, input().split())
    ans = ans + 1 if sum(a) > 1 else ans

print(ans)
