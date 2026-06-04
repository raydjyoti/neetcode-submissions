class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        # Find target loc in m
        # Then, find target loc in n

        left = 0
        right = len(matrix)-1
        nToSearch = -1

        while (left <= right):

            mid = (left + right) // 2
            midL = matrix[mid][0]
            midR = matrix[mid][-1]

            if (midR < target):
                left = mid + 1
            
            elif (midL > target):
                right = mid - 1

            else:
                nToSearch = mid
                break



        if (nToSearch < 0): return False

        left = 0
        right = len(matrix[nToSearch])

        while (left <= right):
            mid = (left + right) // 2
            curr = matrix[nToSearch][mid]

            if (curr < target): left = mid + 1
            elif (curr > target): right = mid - 1
            else: return True

        
        return False