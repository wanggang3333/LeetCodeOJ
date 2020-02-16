class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        children = collections.defaultdict(set)
        for k,v in edges:
            children[k].add(v)
            children[v].add(k)
        roots = set(children.keys())
        while len(roots) >2:
            leaves = [x for x in children if len(children[x]) == 1]
            for x in leaves:
                for y in children[x]:
                    children[y].remove(x)
                del children[x]
                roots.remove(x)
        return list(roots) if n != 1 else [0]
        