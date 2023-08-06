# https://leetcode.com/problems/restore-ip-addresses/submissions/1014118726/

from typing import List


class Solution:
    def rec(self, s: str, res: List[str], curr_ind: int, parts_left: int,
            _len: int, progress: List[str]) -> None:
        if parts_left == 0 and curr_ind != _len:
            return

        if parts_left == 0:
            res.append('.'.join(progress))
            return

        num_per_part = (_len - curr_ind) / parts_left
        if num_per_part > 3 or num_per_part < 1:
            return

        if s[curr_ind] == '0':
            progress.append("0")
            self.rec(s, res, curr_ind + 1, parts_left - 1, _len, progress)
            progress.pop()
            return

        for i in range(curr_ind, min(_len, curr_ind + 3)):
            cur_str = s[curr_ind:(i + 1)]
            cur_int = int(cur_str)
            if cur_int < 0 or cur_int > 255:
                continue

            progress.append(cur_str)
            self.rec(s, res, i + 1, parts_left - 1, _len, progress)
            progress.pop()

    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return []

        res = []
        self.rec(s, res, 0, 4, len(s), [])

        return res
