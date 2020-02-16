class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        while (n % 4 == 0):
            n /= 4
        if (n % 8 == 7):
            return 4
        a = 0
        while a*a <= n:
            b = math.sqrt(n - a*a)
            b = int(b)
            if a*a + b*b == n:
                return bool(a) + bool(b)
            a += 1
        return 3
                
        