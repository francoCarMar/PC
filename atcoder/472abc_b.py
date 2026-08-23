n = int(input())

a = list(map(int, input().split()))

total_sum = sum(a)
part_a = 0
ans = 10 ** 6

for i in range(n - 1):
    part_a += a[i]
    part_b = total_sum - part_a
    ans = min(ans, abs(part_a - part_b))

print(ans)

