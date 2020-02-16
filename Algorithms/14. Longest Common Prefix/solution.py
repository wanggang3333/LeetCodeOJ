class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if strs == []:
            return ''
        for i in range(len(strs)):
            l1 = len(strs[0])
            l2 = len(strs[i])
            if l1 > l2:
                lens = l2
            else:
                lens = l1
            strs[0] = strs[0][0:lens]
            for j in range(lens):
                if strs[0][j] != strs[i][j]:
                    strs[0] = strs[0][0:j]
                    break
        return strs[0]