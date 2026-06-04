class Solution:
    def maxArea(self, height: List[int]) -> int:
        currMax = -1
        left = 0
        right = len(height)-1

        while (left < right):
            lHeight = height[left]
            rHeight = height[right]
            distance = right - left

            if (lHeight < rHeight):
                area = lHeight * distance
                left += 1
            elif (lHeight > rHeight):
                area = rHeight * distance
                right -=1
            else:
                area = lHeight * distance
                left +=1

            if (area > currMax): currMax = area
            
        return currMax

