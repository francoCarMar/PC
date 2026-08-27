class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sig = 1 if x >= 0 else -1
        x = str(abs(x))
        ans = 0
        for i in range(len(x)):
            ans += int(x[i]) * (10 ** i)
        ans = sig * ans
        if ans > 2 ** 31 - 1 or ans < - 2 ** 31:
            return 0
        return ans
