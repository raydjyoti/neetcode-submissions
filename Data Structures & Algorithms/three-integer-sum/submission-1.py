class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nSorted = sorted(nums)

        # Skip 1st num if i+2 = i.. [1, 1, 1], jump to 2nd index
        # Skip 2nd/3rd num if i+1 or i-1 is same

        for i in range(len(nSorted)-2):
            fNum = nSorted[i]

            if (fNum == nSorted[i-1] and i > 0): continue
            # Once i > 0, every next num too will be. Can't sum to 0
            if (nSorted[i] > 0): break

            l = i+1
            r = len(nSorted)-1

            while (l < r):

                lNum = nSorted[l]
                rNum = nSorted[r]

                if (fNum + lNum + rNum == 0):
                    output.append([fNum, lNum, rNum])
                    l+=1
                    r-=1
                    while l < r and nSorted[l] == nSorted[l-1]: l+=1
                    while l < r and nSorted[r] == nSorted[r+1]: r-=1
                elif (fNum + lNum + rNum > 0): r -= 1
                else: l+=1

        return output