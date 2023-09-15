from typing import List, Dict

# https://leetcode.com/problems/reconstruct-itinerary/submissions/1049143699/


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        flights: Dict[str: List[str]] = {}
        for fr, to in tickets:
            a = flights.get(fr, [])
            a.append(to)
            flights[fr] = a

        result = ["JFK"]

        def rec(count: int) -> bool:
            if count == 0:
                return True

            curr_list = flights.get(result[-1], [])
            for i in range(len(curr_list) - 1, -1, -1):
                c = curr_list.pop(i)
                result.append(c)

                if rec(count - 1):
                    return True
                curr_list.insert(i, result.pop())

            return False

        rec(len(tickets))
        return result
