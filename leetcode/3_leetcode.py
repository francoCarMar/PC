class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        start = 0
        end = 0
        for i in range(len(s)):

            ss = set(s[start:end + 1])
            print(len(ss))
            if len(ss) != end - start + 1:
                start += 1
                end += 1
            else:
                end += 1
            ans = max(ans, len(ss))
        return ans