# https://leetcode.com/problems/text-justification/submissions/1032989126/


from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result: List[str] = []
        line: List[str] = []
        length = x = 0

        while x < len(words):
            # length we have + spaces between words we have + curr word length
            if length + len(line) + len(words[x]) > maxWidth:
                spaces, reminder = divmod(maxWidth - length,
                                          max(1, len(line) - 1))  # max - cannot divide by 0

                for i in range(max(1, len(line) - 1)):
                    line[i] += " " * (spaces + 1) if reminder > 0 else " " * spaces
                    reminder -= 1

                result.append("".join(line))
                line, length = [], 0
                continue

            line.append(words[x])
            length += len(words[x])
            x += 1

        last_line = " ".join(line)  # last line is treated differently...
        spaces = maxWidth - len(last_line)
        result.append(last_line + spaces * " ")

        return result