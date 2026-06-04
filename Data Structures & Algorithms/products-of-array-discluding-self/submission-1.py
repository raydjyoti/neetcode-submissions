from collections import deque

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [-1, -1, 0, 0, 0], [0, 0, 0, -9, 3]
        prefix = deque()
        suffix = deque()

        left = 0
        right = len(nums)-1
        lProd = 1
        rProd = 1

        for i in range(len(nums)):
            lNum = nums[left]
            rNum = nums[right]

            lProd *= lNum
            rProd *= rNum

            prefix.append(lProd)
            suffix.appendleft(rProd)

            left += 1
            right -= 1

        output = []

        for i in range(len(nums)):
            totalLeft = 1
            totalRight = 1



            if (i != 0):
                totalLeft = prefix[i-1]

            if (i != len(nums)-1): totalRight = suffix[i+1]


            total = totalLeft * totalRight
            output.append(total)

        return output