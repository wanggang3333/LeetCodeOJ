class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        nums = []
        ans = 0
        size = len(words)
        for word in words:
            print [1<<(ord(x)-ord('a')) for x in set(word)]
            nums.append(sum([1<<(ord(x)-ord('a')) for x in set(word)]))
            
        print "nums:", nums
        for x in range(size):
            for y in range(x+1, size):
                if nums[x] & nums[y] == 0:
                    ans = max(ans, len(words[x])*len(words[y]))
                    
        return ans