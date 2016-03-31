class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0]
        for n in range(1,num+1):
            #ans.append(ans[n>>1]+(n&1))
            
            ans.append(ans[n-(1<<int(math.log(n,2)))] + 1)
        return ans