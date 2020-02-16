class Solution:
    # @return an integer
    def reverse(self, x):
        ret = 0
        flag = 1
        if x < 0:
            flag = -1
            x *= -1
        while(x!=0):
            ret = ret*10+x%10
            x = x/10
        print flag *ret
        if flag *ret > 2147483647 or ret * flag < -2147483648:
            return 0
        return ret*flag