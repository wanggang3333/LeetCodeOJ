class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ROMAN = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        n =len(s) - 1
        sum = ROMAN[s[0]]
        for i in range(n):
            pre = ROMAN[s[i]]
            post = ROMAN[s[i+1]]
            if pre >= post:
                sum += post
            else:
                sum = sum - 2 * pre + post
                
        return sum