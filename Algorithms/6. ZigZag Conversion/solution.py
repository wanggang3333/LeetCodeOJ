class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if s == '' or len(s) <= numRows or numRows == 1:
            return s
        result = ''
        
        for i in range(numRows):
            j = i
            k = 0
            result += s[j]
            while j < len(s):
                if i == 0 or i == numRows -1:
                    j += 2*numRows - 2
                elif k == 0:
                    j += 2*(numRows - i -1)
                    k = 1
                else:
                    j += 2*i
                    k = 0
                if j < len(s):
                    result += s[j]
        return result