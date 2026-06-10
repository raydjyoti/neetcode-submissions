class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        highest = nums[0]
        lowest = nums[0]
        output = highest

        for n in nums[1:]:
            highTemp = highest
            highest = max(n, n*highest, n*lowest)
            lowest = min(n, n*lowest, n*highTemp)
            output = max(output, highest)


        return output