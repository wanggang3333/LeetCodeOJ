class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        i = 0
        maxArea = 0
        heights.append(0)
        n = len(heights)
        while i < n:
            if (stack == []) or heights[stack[-1]] <= heights[i]:
                stack.append(i)
                i += 1
            else:
                t = stack.pop()
                maxArea = max(maxArea, heights[t]*(i if not stack else i - stack[-1]-1))
        return maxArea