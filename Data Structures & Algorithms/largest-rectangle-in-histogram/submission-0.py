class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # A. When encounter higher, keep adding to stack
        # B. When encounter lower, calc area for each
            # Right pointer set to highest stack end
            # Left pointer changes with pop
            # After done, B. this lower points left pointer will be last cal in stack.

        stack = []
        maxArea = 0

        for i in range(len(heights)):

            leftPoint = i

            while (len(stack) > 0 and heights[i] < heights[stack[-1][1]]) :
                stackEnd = stack.pop()
                leftPoint = stackEnd[0]
                rightPoint = i
                width = rightPoint - leftPoint
                height = heights[stackEnd[1]]
                area = width * height
                maxArea = max(maxArea, area)

            stack.append([leftPoint, i])


        if (len(stack) > 0):
            rightPoint = stack[-1][1] + 1
            while (len(stack) > 0):
                stackEnd = stack.pop()
                leftPoint = stackEnd[0]
                width = rightPoint - leftPoint
                height = heights[stackEnd[1]]
                area = width * height
                maxArea = max(maxArea, area)

        return maxArea
