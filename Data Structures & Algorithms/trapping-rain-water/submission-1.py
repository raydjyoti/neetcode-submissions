class Solution:
    def trap(self, height: List[int]) -> int:
        # Keep track of left max, right max
        # Water stored = max(left, right) - curr
        # Move the pointer which has min left/right

        left = 0
        right = len(height)-1
        lmax = 0
        rmax = 0
        total = 0

        while (left <= right):
            currL = height[left]
            currR = height[right]

            if (currL < min(lmax, rmax)):
                total += min(lmax, rmax) - currL

            elif (currR < min(lmax, rmax)):
                total += min(lmax, rmax) - currR

            lmax = max(currL, lmax)
            rmax = max(currR, rmax)

            if (lmax > rmax): right -= 1
            elif (rmax > lmax): left += 1
            else:
                left += 1

        return total



