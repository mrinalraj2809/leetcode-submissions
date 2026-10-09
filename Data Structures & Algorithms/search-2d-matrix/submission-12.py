class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) -1
        pos = -1
        while(l<=r):
            mid = int((l + r)/2)
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                pos = mid
                break
            elif target > matrix[mid][0]:
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid - 1
        if pos == -1:
            return False
        l = 0
        r = len(matrix[pos]) - 1
        while(l <= r):
            mid = int(math.floor((l+r)/2))

            if target == matrix[pos][mid]:
                return True
            elif target > matrix[pos][mid]:
                l = mid + 1
            else:
                r = mid - 1
        return False
        