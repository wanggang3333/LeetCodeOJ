class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return self.combine2(1,n+1,k)
        
        
    def combine2(self,l,r,k):
        n = r - l
        if n == 0:
            return []
        if k == 1:
            return [[i] for i in range(l,r)]
        if k > n:
            return []
        if k == n:
            return [[i for i in range(l,r)]]
        res = []
        for i in range(l,r):
            for j in self.combine2(i+1,r,k-1):
                res.append([i]+j)
        return res