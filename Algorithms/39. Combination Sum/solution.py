class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        Solution.res = []
        self.DFS(candidates, target, 0, [])
        return Solution.res
        
    def DFS(self, candidates, target, start, itemList):
        n = len(candidates)
        if target == 0:
            Solution.res.append(itemList)
        for i in range(start, n):
            if target < candidates[i]:
                return 
            self.DFS(candidates, target-candidates[i],i,itemList+[candidates[i]])