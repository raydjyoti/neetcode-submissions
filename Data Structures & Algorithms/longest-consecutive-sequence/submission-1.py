class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)

        maxCount = 0

        for n in numSet:
            count = 0

            if (n-1 not in numSet):
                curr = n

                while (curr in numSet):
                    count += 1
                    curr += 1

            maxCount = max(maxCount, count)

        return maxCount
