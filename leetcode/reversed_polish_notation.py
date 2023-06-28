# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
#
# Evaluate the expression. Return an integer that represents the value of the expression.
#
# Note that:
#
# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

from typing import List
from math import trunc

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack: List[int] = []

        for elem in tokens:
            if (elem.lstrip('-')).isnumeric():
                num_stack.append(int(elem))
                continue

            last = num_stack.pop()
            pre = num_stack.pop()

            if elem == "+":
                num_stack.append(pre + last)

            elif elem == "-":
                num_stack.append(pre - last)

            elif elem == "*":
                num_stack.append(pre * last)

            elif elem == "/":
                num_stack.append(trunc(pre / last))

        return num_stack[-1]


