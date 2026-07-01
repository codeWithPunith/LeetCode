class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        # -----------------------------
        # STEP 1: Multi-source BFS
        # Compute distance to nearest thief for every cell
        # -----------------------------
        dist = [[-1] * n for _ in range(n)]
        q = deque()

        # push all thief cells (value = 1)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
                    dist[i][j] = 0

        # BFS from all thieves simultaneously
        while q:
            r, c = q.popleft()

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        # -----------------------------
        # STEP 2: Dijkstra (max-heap)
        # maximize minimum safeness along path
        # -----------------------------
        maxHeap = []
        visited = [[False] * n for _ in range(n)]

        # start from (0,0), initial safeness = dist[0][0]
        heapq.heappush(maxHeap, (-dist[0][0], 0, 0))

        while maxHeap:
            safeness, r, c = heapq.heappop(maxHeap)
            safeness = -safeness

            # if reached destination → answer found
            if r == n - 1 and c == n - 1:
                return safeness

            if visited[r][c]:
                continue
            visited[r][c] = True

            # explore neighbors
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    # path safeness = min(current path, next cell safety)
                    new_safeness = min(safeness, dist[nr][nc])

                    heapq.heappush(
                        maxHeap,
                        (-new_safeness, nr, nc)
                    )

        return 0