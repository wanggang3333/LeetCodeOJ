class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a','e','i','o','u']
        size = len(s)
        ls = list(s)
        i, j = 0, size-1
        while True:
            while i < size and ls[i].lower() not in vowels:
                i += 1
            while j >= 0 and ls[j].lower() not in vowels:
                j -= 1
            if i >= j:
                break
            else:
                ls[i] ,ls[j] = ls[j], ls[i]
                i += 1
                j -= 1
        return ''.join(ls)