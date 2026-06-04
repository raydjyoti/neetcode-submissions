class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        numsSorted = sorted(nums)

        # [-4, -1, -1, 0, 1, 2]

        for i in range(len(numsSorted)):
            num1 = numsSorted[i]
            if (num1 > 0): break
            if (i > 0 and numsSorted[i] == numsSorted[i-1]): continue

            j = i+1
            k = len(numsSorted)-1

            while (j < k):
                num2 = numsSorted[j]
                num3 = numsSorted[k]

                if (j > i+1 and numsSorted[j] == numsSorted[j-1]):
                    j+=1
                    continue
                if (k<len(numsSorted)-1 and numsSorted[k] == numsSorted[k+1]):
                    k-=1
                    continue


                if (num1+num2+num3 == 0):
                    output.append([num1, num2, num3])
                    j+=1
                    k-=1
                if (num1+num2+num3 > 0): k-=1
                if (num1+num2+num3 < 0): j+=1

        return output