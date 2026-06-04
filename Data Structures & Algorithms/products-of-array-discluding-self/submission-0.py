from collections import deque

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # [1, 1, 2, 6] - ltr
        # [24, 12 , 4, 1] - rtl

        # [1, -1, -1, 0, 0] - ltr
        # [0, 0 ,-9, 3, 1] - rtl

        ltr = deque()
        rtl = deque()

        l = 0
        r = len(nums)-1

        lProduct = 1
        rProduct = 1

        while (l < len(nums)):

            ltr.append(lProduct)
            rtl.appendleft(rProduct)

            lProduct *= nums[l]
            rProduct *= nums[r]

            l+=1
            r-=1

        print(ltr)
        
        output = []

        for i in range(len(ltr)):
            prod = ltr[i]*rtl[i]
            output.append(prod)

        return output