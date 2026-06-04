import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h = [3,6,7,11]
        # h[-1] = 11/hour fastest way to finish stack.
        # Fastest speed = max value from piles
        # Slowest speed = 1
        # Binary search to find min value
        # Time to eat = math.ceil(pile size/speed) = 11/11 = 1 hour
        # [30,11,23,4,20] => [1,2,3,4,5,6....,26,27,28,29,30]

        pSorted = sorted(piles, reverse=True)
        left = 1
        right = pSorted[0]
        slowest = right

        def checkComplete(perHour):
            total = 0
            for i in range(len(pSorted)):
                bananas = pSorted[i]
                ttc = math.ceil(bananas/perHour)
                total += ttc

                if (total > h): return False

            return True


        while (left <= right):
            mid = (left + right) // 2
            isComplete = checkComplete(mid)

            if (isComplete):
                slowest = min(mid, slowest)
                right = mid-1
            
            else:
                left = mid+1

        return slowest

