class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 0 - {0:1}
        # 3 - {0:1, 3:1}
        # 7 - {0:1, 3:1, 7:1}
        # 2 - {0:1, 7:1, 3:2, 2:2} -> Boundary = [2, 3]
        # 5 - {0:1, 7:1, 3:2, 2:2, 5:1}
        # 8 - {0:1, 7:2, 3:2, 2:2, 5:1, 8:2} -> Boundary = [7, 8]
        # 4 - {0:1, 7:2, 3:2, 2:4, 5:4, 8:2, 4:4} -> Boundary = [2, 5]
        # 6 - {0:1, 7:2, 3:2, 2:7, 5:4, 8:7, 4:4} -> [2, 8]
        # 0 - xx
        # 1 - {0:9}

        # 3:1, 4:1, 5 -> 

        store = {}
        maxCount = 0

        for num in nums:
            if (num in store): continue

            leftVal = store.get(num-1) or 0
            rightVal = store.get(num+1) or 0

            total = leftVal + 1 + rightVal
            maxCount = max(maxCount, total)

            store[num] = total
            store[num-leftVal] = total
            store[num+rightVal] = total
        
        return maxCount







