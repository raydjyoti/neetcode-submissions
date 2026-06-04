class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums)-1

        while (left <= right):
            mid = (left + right) // 2
            curr = nums[mid]

            if (curr < target):
                left = mid + 1

            elif (curr > target):
                right = mid - 1

            else: return mid

        return -1