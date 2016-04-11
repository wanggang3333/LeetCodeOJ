class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        maxlen = 0
        table = [-1 for i in range(256)]
        for i in range(len(s)):
            if table[ord(s[i])] != -1:
                while start <= table[ord(s[i])]:
                    table[ord(s[start])] = -1
                    start += 1
            if i - start + 1 > maxlen: maxlen = i - start + 1
            table[ord(s[i])] = i
        return maxlen