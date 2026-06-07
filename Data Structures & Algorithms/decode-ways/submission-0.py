class Solution:
    def numDecodings(self, s: str) -> int:

        self.store = {}

        def dfs(i):
            
            if i in self.store: return self.store[i]

            if i >= len(s): return 1
            if s[i] == "0": return 0


            count = dfs(i+1)
            if i < len(s)-1 and int(s[i:i+2]) <= 26:
                count += dfs(i+2)

            self.store[i] = count
            return count

        return dfs(0)