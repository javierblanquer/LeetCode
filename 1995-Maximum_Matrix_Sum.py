from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        negative_items = len([item for sub_item in matrix for item in sub_item if(item < 0)])
        total = sum([abs(item) for sub_item in matrix for item in sub_item])
        if(negative_items % 2 == 0):
            return total
        else:
            return total - 2 * abs(min((item for subitem in matrix for item in subitem),key=abs))

matrix1 = [[1,-1],[-1,1]]
matrix2= [[1,2,3],[-1,-2,-3],[1,2,3]]
matrix3= [[-1,0,-1],[-2,1,3],[3,2,2]]
testing = Solution()
test =testing.maxMatrixSum(matrix=matrix1)
print(test)
test2 =testing.maxMatrixSum(matrix=matrix2)
print(test2)
test3 =testing.maxMatrixSum(matrix=matrix3)
print(test3)
matrix4 = [[2,9,3],[5,4,-4],[1,7,1]]
test4 = testing.maxMatrixSum(matrix=matrix4)
print