class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Define left, right and mid
        # [7,0,1,2,3,4,5,6]

        left = 0
        right = len(nums)-1

        while (left <= right):

            mid = (left + right) // 2
            leftN = nums[left]
            rightN = nums[right]
            midN = nums[mid]

            if midN == target: return mid
            
            leftSorted = False
            rightSorted = False
            
            if (midN <= rightN): rightSorted = True
            elif (midN >= leftN): leftSorted = True

            if (target > midN):
                if rightSorted:
                    if target <= rightN: left = mid+1
                    else: right = mid-1

                else: left = mid+1

            elif (target < midN):
                if leftSorted:
                    if target >= leftN: right = mid-1
                    else: left = mid+1

                else: right = mid-1

            else: break

        return -1




            
