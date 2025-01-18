import heapq

class Solution:
    def minCost(self, grid):
        n, m = len(grid), len(grid[0])
        pq = []
        heapq.heappush(pq, (0, 0, 0))  # (cost, row, col)
        vis = [[0] * m for _ in range(n)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while pq:
            d, r, c = heapq.heappop(pq)
            if vis[r][c]:
                continue
            vis[r][c] = 1
            if r == n - 1 and c == m - 1:
                return d
            dir = grid[r][c] - 1
            nr, nc = r + directions[dir][0], c + directions[dir][1]
            if self.isValid(nr, nc, n, m, vis):
                heapq.heappush(pq, (d, nr, nc))
            for i in range(4):
                if i == dir:
                    continue
                nr, nc = r + directions[i][0], c + directions[i][1]
                if self.isValid(nr, nc, n, m, vis):
                    heapq.heappush(pq, (d + 1, nr, nc))
        return -1

    def isValid(self, r, c, n, m, vis):
        return 0 <= r < n and 0 <= c < m and not vis[r][c]