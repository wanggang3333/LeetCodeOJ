class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        Solution.result = ['JFK']
        Solution.length = len(tickets)
        graph = collections.defaultdict(list)
        for a,b in tickets:
            graph[a].append(b)
        self.dfs('JFK', graph)
        return Solution.result
        
        
        
    def dfs(self, start, graph):
        if len(Solution.result) == Solution.length + 1:
            return True
            
        currDes = sorted(graph[start])
        for des in currDes:
            graph[start].remove(des)
            Solution.result.append(des)
            
            valid = self.dfs(des, graph)
            if valid: return True
            Solution.result.pop()
            graph[start].append(des)