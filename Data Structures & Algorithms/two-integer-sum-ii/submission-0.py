class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Constant space
        # [1, 2, 3, 4, 7, 9, 11, 12, 14] target = 20

        left = 0
        right = len(numbers)-1

        if (len(numbers) == 2): return [1,2]

        while (True):
            lNum = numbers[left]
            rNum = numbers[right]
            complement = target-rNum

            if (lNum == complement): return [left+1, right+1]
            elif (lNum < complement):
                left +=1
            elif (lNum > complement):
                right-=1
        