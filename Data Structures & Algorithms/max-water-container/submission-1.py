class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        output = 0

        while (left < right):
            distance = right - left
            l = height[left]
            r = height[right]

            water = min(l, r) * distance
            output = max(output, water)

            if (l < r): left += 1
            else: right -= 1

        return output