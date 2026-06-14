class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [-1] * len(nums)

        def dfs(prevNum, currInd):

            if currInd >= len(nums): return 0

            count = 0

            if dp[currInd] != -1: return dp[currInd]

            for i in range(currInd, len(nums)):

                if nums[i] > prevNum:
                    count = max(1 + dfs(nums[i], i+1), count)

            dp[currInd] = count
            return count



        return dfs(float('-inf'), 0)