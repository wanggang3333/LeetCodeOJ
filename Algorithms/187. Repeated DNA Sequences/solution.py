class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        key = 0
        res = []
        maps = {}
        for i in range(len(s)):
            key = (key<<2)+self.toInt(s[i]) & 0xfffff
            if i <9:
                continue
            if maps.has_key(key):
                if maps[key] == 1:
                    res.append(s[i-9:i+1])
                maps[key] = maps[key]+1
            else:
                maps[key] = 1
        return res
            
    def toInt(self, s):
        if s == 'A':
            return 0
        if s == 'C':
            return 1
        if s == 'G':
            return 2
        if s == 'T':
            return 3
        