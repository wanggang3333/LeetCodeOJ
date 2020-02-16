class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations = sorted(citations)[::-1]
        index = 0
        for item in citations:
            if item >= index + 1:
                index += 1
            else:
                break
        return index