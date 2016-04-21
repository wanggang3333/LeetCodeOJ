class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        strs = path.split('/')
        items = []
        for i in strs:
            if i == '.' or i == '':
                continue
            elif i == '..':
                if items != []:
                    items.pop()
            else:
                items.append(i)
        if items == []:
            return '/'
        res = ''
        for i in items:
            res += "/"+i
        return res        
        