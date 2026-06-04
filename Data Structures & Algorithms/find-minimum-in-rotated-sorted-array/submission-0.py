class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [4,5,6,7,8,9,10,1,2,3]
        # Define left, right and mid
        # If mid > right, smaller num on right half
        # left = mid + 1, find mid, repeat.
        # If mid < right, check if mid < left

        minVal = float('inf')
        left = 0
        right = len(nums)-1
        mid = (left+right)//2

        while (left <= right):
            mid = (left+right)//2
            minVal = min(minVal, nums[mid])

            if (nums[mid] > nums[right]):
                left = mid + 1
            else:
                right = mid-1
        
        return minVal

