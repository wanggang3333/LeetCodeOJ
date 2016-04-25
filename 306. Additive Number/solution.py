class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        def isValid(num):
            return len(num) == 1 or num[0] != '0'
            
        def search(a,b,c):
            d = str(int(a) + int(b))
            if not isValid(d) or not c.startswith(d):
                return False
            if c == d:
                return True
            return search(b,d,c[len(d):])
            
        for x in range(1,len(num)/2+1):
            for y in range(x+1,len(num)):
                a,b,c = num[:x],num[x:y],num[y:]
                if not isValid(a) or not isValid(b):
                    continue
                if search(a,b,c):
                    return True
        return False