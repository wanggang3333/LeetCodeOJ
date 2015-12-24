class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        res = 1
        flag = 0
        if n < 0:
            flag = 1 # n为负数标志
            n = -n
        while n > 0:
            if n%2 == 1:
                res = res * x
            x = x*x
            n = n/2
        if flag == 1:
            return 1/res
        else:
            return res