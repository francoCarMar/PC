class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        ans = ""
        if numRows == 1:
            return s
        for r in range(numRows):
            for i in range(r, len(s), numRows * 2 - 2):
                ans += s[i]
                next_pos = i + (numRows - r ) * 2 - 2
                if r != 0 and r != numRows - 1 and next_pos < len(s):
                    ans += s[next_pos]
        return ans
