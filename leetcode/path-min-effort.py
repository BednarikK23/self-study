import math
from typing import List
from heapq import heappop, heappush

# https://leetcode.com/problems/path-with-minimum-effort/submissions/1051015433/


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        h, w = len(heights), len(heights[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        dist = [[math.inf for _ in range(w)] for _ in range(h)]
        dist[0][0] = 0

        heap = [(0, 0, 0)]
        while heap:
            diff, x, y = heappop(heap)

            if x == w - 1 and y == h - 1:
                return diff

            for x1, y1 in directions:
                nx, ny = x + x1, y + y1
                if nx < 0 or nx >= w or ny < 0 or ny >= h:
                    continue

                curr = abs(heights[y][x] - heights[ny][nx])
                curr = max(curr, diff)

                if curr < dist[ny][nx]:
                    dist[ny][nx] = curr
                    heappush(heap, (curr, nx, ny))
