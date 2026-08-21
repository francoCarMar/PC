def solve():
    n = int(input())

    arr = list(map(int, input().split()))
    arr.append(0)
    arr = sorted(arr)

    pos = arr.index(0)
    ans = 0
    pos_left, pos_right = pos - 1, pos + 1 
    for _ in range(n):
        if pos == 0:
            ans += abs(arr[pos] - arr[-1])
            return ans
        elif pos == n:
            ans += abs(arr[pos] - arr[0])
            return ans
        else:
            diff_left = abs(arr[pos] - arr[pos_left])
            diff_right = abs(arr[pos] - arr[pos_right])
            if diff_left <= diff_right:
                pos = pos_left
                pos_left = pos - 1
            else:
                pos = pos_right
                pos_right = pos + 1
            ans += min(diff_left , diff_right)
    return ans
print(solve())
