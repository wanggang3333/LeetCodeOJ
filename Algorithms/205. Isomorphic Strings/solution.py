class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = len(s); n = len(t)
        if m != n:
            return False
        sDict = {}; tDict = {}
        for i in range(m):
            if sDict.has_key(s[i]):
                if sDict[s[i]] != t[i]:
                    return False
            else:
                sDict[s[i]] = t[i]
        for i in range(m):
            if tDict.has_key(t[i]):
                if tDict[t[i]] != s[i]:
                    return False
            else:
                tDict[t[i]] = s[i]
        return True
        
        
        