#Time complexity = O(m*n)
# Space Complexity = O(m*n)
from collections import deque

class Solution:
    def orangesRotting(self, grid) -> int:
        rows=len(grid)
        columns = len(grid[0])
        queue = deque()
        fresh_oranges = 0

        for i in range(0,rows):
            for j in range(0,columns):

                if grid[i][j]==1:
                    fresh_oranges+=1

                if grid[i][j]==2:
                    queue.append([i,j])
        
        if fresh_oranges == 0:
            return 0

        time = 0

        while len(queue)>=1 and fresh_oranges>0:
            size = len(queue)
            for i in range(0,size):
                r,c = queue.popleft()

                if c-1>=0 and grid[r][c-1]==1:
                    grid[r][c-1]=2
                    queue.append([r,c-1])
                    fresh_oranges -=1
                
                if c+1<columns and grid[r][c+1]==1:
                    grid[r][c+1]=2
                    queue.append([r,c+1])
                    fresh_oranges -=1


                if r-1>=0 and grid[r-1][c]==1:
                    grid[r-1][c]=2
                    queue.append([r-1,c])
                    fresh_oranges -=1

                if r+1<rows and grid[r+1][c]==1:
                    grid[r+1][c]=2
                    queue.append([r+1,c])
                    fresh_oranges -=1
            time +=1

        if fresh_oranges>0:
            return -1
        
        return time
                





            

        


        