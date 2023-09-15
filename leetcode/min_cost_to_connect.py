import heapq
from typing import List, Set, Tuple

# https://leetcode.com/problems/min-cost-to-connect-all-points/submissions/1049976905/


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        que: List[Tuple[int, Tuple[int, int]]] = []
        heapq.heappush(que, (0, (points[0][0], points[0][1])))

        visited: Set[Tuple[int, int]] = set()

        count, result = 0, 0
        while que:
            dist, point = heapq.heappop(que)
            if point in visited:
                continue

            visited.add(point)
            result += dist
            count += 1
            if len(points) == count:
                return result

            x0, y0 = point
            for x1, y1 in points:
                if (x1, y1) in visited:
                    continue
                d = abs(x0 - x1) + abs(y0 - y1)
                heapq.heappush(que, (d, (x1, y1)))

        return result
