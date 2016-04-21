class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        if num <= 0:
            return False
        print num ,num >>1
        return (num&(num-1)) == 0 and num & 0x55555555 > 0