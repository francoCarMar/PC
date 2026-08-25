class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                ss = s[i: j + 1]
                ans = ss if len(ss) > len(ans) and ss == ss[::-1] else ans
        return ans