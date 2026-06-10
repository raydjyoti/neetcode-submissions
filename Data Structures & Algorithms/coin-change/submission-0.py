class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount+1)

        def dfs(rem):
            
            if rem == 0: return 0
            if rem < 0: return float('inf')

            if dp[rem] != 0: return dp[rem]
            coinsTaken = float('inf')

            for c in coins:
                coinsTaken = min(1+dfs(rem-c), coinsTaken)

            dp[rem] = coinsTaken
            return coinsTaken



        dfs(amount)

        if dp[amount] == float('inf'): return -1
        else: return dp[amount]