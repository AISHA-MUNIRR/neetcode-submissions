class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows=len(grid)
        cols=len(grid[0])
        path=set()
        num_path=0

        def dfs(r, c):

            if (r<0 or c<0 or
            r>=rows or c>=cols or
            grid[r][c]!='1' or
            (r,c) in path):
                return False

            path.add((r,c))

            dfs(r+1,c) 
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            
            return True
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c):
                    num_path+=1
        return num_path
                

        



        