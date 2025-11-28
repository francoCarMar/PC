k, n, w = map(int, input().split())

ans = n - k * w * (w + 1) // 2
if ans > 0:
    print(0)
else:
    print(abs(ans))