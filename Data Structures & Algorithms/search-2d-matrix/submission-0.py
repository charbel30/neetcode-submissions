class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(len(matrix)):
            if target > matrix[i][-1]:
                continue
            
            l, r = 0 , len(matrix[i]) - 1
            while l <= r:
                m = l + ((r-l) // 2 )
                if matrix[i][m] < target:
                    l = m + 1
                elif matrix[i][m] > target:
                    r = m - 1
                else:
                    return True
            return False
        

        return False