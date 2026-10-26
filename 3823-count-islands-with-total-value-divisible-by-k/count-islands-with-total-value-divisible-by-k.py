class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(i, j):
            total = grid[i][j]
            grid[i][j] = 0

            for di, dj in [(1, 0), (-1, 0),
                           (0, 1), (0, -1)]:
                x, y = i + di, j + dj

                if (0 <= x < m and 0 <= y < n
                        and grid[x][y] > 0):
                    total += dfs(x, y)

            return total

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    total = dfs(i, j)

                    if total % k == 0:
                        count += 1

        return count