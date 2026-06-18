class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows=len(matrix)
        cols=len(matrix[0])
        zero_list=[]
        for i in range(rows):
            for j in range (cols):
                if matrix[i][j]==0:
                    zero_list.append((i,j))       
        
        for i,j in zero_list:
            for zero in range(rows):
                matrix[zero][j]=0

            for zero in range(cols):
                matrix[i][zero]=0