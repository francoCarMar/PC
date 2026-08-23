input = __import__("sys").stdin.readline
n, q = tuple(map(int, input().split()))

base = [0] * n
ans = []
idxs = []
xor = 0

for _ in range(q):
    a = list(map(int, input().split()))

    if a[0] == 1:
        idx = a[1] - 1
        if base[idx] == 0:
            idxs.append(idx)
        base[idx] += 1
        xor ^= (base[idx] - 1) ^ base[idx]
    else:
        for idx in idxs:
            base[idx] -= 1
            xor ^= (base[idx] + 1) ^ base[idx]
        idxs = [idx for idx in idxs if base[idx] > 0]
    print(xor)

