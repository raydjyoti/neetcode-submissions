class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        self.output = []
        
        def dfs(total, ind, arr):

             if ind >= len(candidates): return
             if total > target: return

             if total == target: self.output.append(arr)

             for i in range(ind, len(candidates)):
                curr = candidates[i]
                newArr = list(arr)
                newArr.append(curr)
                dfs(total+curr, i, newArr)

        dfs(0, 0, [])

        return self.output