# https://leetcode.cn/problems/number-of-islands/
#【岛屿数量】深搜
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[0] * n for i in range(m)]
        result = 0

        def dfs(x, y):
            nonlocal grid, visited
            dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            print(f'nextx, nexty:{x, y}')
            if (grid[x][y] == "0" or visited[x][y] == 1):
                # 如果遇到海水或visited打过标，即dfs已经最深了，退出dfs
                return
            visited[x][y] = 1 # 一旦走过就打标，再做一些判断后，下次碰到打过标的可以直接略过
            for i in range(4):
                nextx = x + dir[i][0]
                nexty = y + dir[i][1]
                if (nextx >= m or nextx < 0 or nexty >= n or nexty <0): # m n容易写错
                    # 出界就换下一个i                                # return
                    continue # 不能是return
                

                # print(f'nextx, nexty: {nextx}, {nexty}')
                # visited[nextx][nexty] = 1
                dfs(nextx, nexty)

        for i in range(m):
            for j in range(n):
                if (grid[i][j] == "1" and visited[i][j] == 0):
                # 如果是陆地且没有走过(即visited没有打过标)
                    result += 1
                    print(f'{i}, {j}')                          
                    dfs(i, j)
                    
        
        return result
