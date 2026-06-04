class Solution:
    def trap(self, height: List[int]) -> int:
        # Left max/Right max
        # If both taller, min(lmax, rmax) - height
        # Find max
        # Traverse 2 points to reach it

        maxHeight = -1
        maxIndex = -1

        for i in range(len(height)):
            if (height[i] > maxHeight):
                maxHeight = height[i]
                maxIndex = i

        left = 0
        right = len(height)-1
        total = 0

        leftMax = -1
        rightMax = -1

        while (left < maxIndex or right > maxIndex):

            if (left < maxIndex):
                if (leftMax > height[left]):
                    total += (leftMax - height[left])

                elif (leftMax < height[left]):
                    leftMax = height[left]
                
                left += 1

            if (right > maxIndex):
                if (rightMax > height[right]):
                    total += (rightMax - height[right])

                elif (rightMax < height[right]):
                    rightMax = height[right]

                right -= 1

        return total

