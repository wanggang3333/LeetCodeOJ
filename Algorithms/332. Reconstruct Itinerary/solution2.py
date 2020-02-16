class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        result = []
        graph = collections.defaultdict(list)
        for a,b in sorted(tickets)[::-1]:
            graph[a].append(b)
            
        def visit(start):
            while graph[start]:
                visit(graph[start].pop())
            result.append(start)
            
        visit('JFK')
        return result[::-1]