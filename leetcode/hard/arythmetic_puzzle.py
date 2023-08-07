# https://leetcode.com/problems/verbal-arithmetic-puzzle/submissions/1015061142/
# its rough on memory but the reason is that, i programmed this, so it can
# tell the real value of each letter not just bool is_solvable...

from typing import Optional, Dict, List, Set


class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        return solve(words, result, 10) is not None


StrInt = Dict[str, int]
IntStr = Dict[int, str]


def final_letter(curr_char: str, summ: int, base: int,
                 letterDigit: Dict[str, int],
                 digitLetter: Dict[int, str]) -> Optional[Dict[str, int]]:
    """
    we are on final char "result" of equation,
    when the mapping for equation is correct return Dict else return None
    for more see <arythmetic_rec>
    """
    if curr_char in letterDigit:
        digit = letterDigit[curr_char]

        if digit != 0 and digit == summ:
            return letterDigit

        return None

    wanted_digit = summ % base
    digit_used = wanted_digit in digitLetter

    if wanted_digit != 0 and wanted_digit == summ and not digit_used:
        digitLetter[wanted_digit] = curr_char
        letterDigit[curr_char] = wanted_digit

        return letterDigit
    return None


def new_char_in_equals(curr_char: str, summ: int, base: int, left: List[str],
                       equals: str, col: int, letterDigit: Dict[str, int],
                       digitLetter: Dict[int, str], _first_letters: Set[str]) \
        -> Optional[Dict[str, int]]:
    """
    we have current char, in the "result" word, we know that char wasn't used,
    we look for ideal digit using modulo, if this digit cannot be used we
    return None else we go deeper into recursion... (to next column and 1. row)
    for more see <arythmetic_rec>
    """

    digit = summ % base
    if digit == 0 and curr_char in _first_letters:
        return None

    digit_used = digit in digitLetter

    if digit_used:
        if curr_char != digitLetter[digit]:
            return None

        return arythmetic_rec(left, equals, base, 0,
                              col + 1, letterDigit,
                              digitLetter, summ // base, _first_letters)

    # if not digit_used:
    digitLetter[digit] = curr_char
    letterDigit[curr_char] = digit

    res = arythmetic_rec(left, equals, base, 0,
                         col + 1, letterDigit,
                         digitLetter, summ // base, _first_letters)
    if res is not None:
        return res

    digitLetter.pop(digit)
    letterDigit.pop(curr_char)
    return None


def old_char_in_equals(digit: int, summ: int, base: int, left: List[str],
                       equals: str, col: int, letterDigit: Dict[str, int],
                       digitLetter: Dict[int, str],
                       _first_letters: Set[str]) -> Optional[Dict[str, int]]:
    """
    just look if sum of left side is equal to our given digit,
    then it returns None or goes deeper to the recursion
    for more see <arythmetic_rec>
    """
    if summ % base == digit:

        res = arythmetic_rec(left, equals, base, 0,
                             col + 1, letterDigit,
                             digitLetter, (summ // base), _first_letters)

        return res
    return None


def new_char_equation(curr_char: str, left: List[str], equals: str, base: int,
                      col: int, row: int, letterDigit: Dict[str, int],
                      digitLetter: Dict[int, str], summ: int,
                      _first_letters: Set[str]) -> Optional[Dict[str, int]]:
    """
    using for cycle we backtrack over digits that we map onto current char
    for more see arythmetic_rec
    """
    for digit in range(base):
        if digit == 0 and curr_char in _first_letters:
            continue

        if digit in digitLetter:
            continue

        letterDigit[curr_char] = digit
        digitLetter[digit] = curr_char

        res = arythmetic_rec(left, equals, base, row + 1,
                             col, letterDigit,
                             digitLetter, summ + digit, _first_letters)

        if res is not None:
            return res

        digitLetter.pop(digit)
        letterDigit.pop(curr_char)

    return None


def arythmetic_rec(_left: List[str], _equals: str, _base: int,
                   row: int, col: int, letterDigit: Dict[str, int],
                   digitLetter: Dict[int, str], summ: int,
                   _first_letters: Set[str]) -> Optional[Dict[str, int]]:
    """
    using backtracking trying to map right digits to letters
    we have:
        A + ... + B = C
    we distinguish different possibilities that may arise:
        1. we get to the final letter - last letter in c
        2. are somewhere in C
            a) the letter has value - check if correct, continue/go back
                                    - check <summ % base == letter>
            b) the letter has no value - assign value if value not taken
                                       - <letter = summ % base>
        3. we re somewhere in A + ... + B
            a) the letter has value - check if correct, continue/go back
            b) the letter has no value - assign value if value not taken
                        if backtrack back here with None try another val...
            c) the word is shorter then parameter <row> - there is no letter
                                                        in this word
    imagine:
       A
    + ...
    +  B
    =  C
    so every time we re on left side - A-B we increase <row> to get to the next
    member, if we re in result, C, we set <row = 0> and increase col so we get
    to the next letters...
    we accumulate the <summ> if we re in C we add reminder to the next col -
    - <summ // base>
    """

    # word1 + word2 + word3 + ... + wordN  =  EQUALS
    # _________LEFT_____________________     __RIGHT_

    # ---------------------< RIGHT SIDE >---------------------
    if row == len(_left):
        char: str = _equals[col]
        row_size = len(_equals)

        if row_size - 1 == col:
            # 1
            return final_letter(char, summ, _base, letterDigit, digitLetter)

        if char not in letterDigit:
            # 2.b)
            return new_char_in_equals(char, summ, _base, _left, _equals, col,
                                      letterDigit, digitLetter, _first_letters)

        # if char in letterDigit:
        # 2.a)
        digit = letterDigit[char]

        return old_char_in_equals(digit, summ, _base, _left, _equals, col,
                                  letterDigit, digitLetter, _first_letters)

    # ---------------------< LEFT SIDE >---------------------
    if row < len(_left):
        curr_row = _left[row]
        row_size = len(curr_row)

        if col >= row_size:
            # no letter in this word so move to next member - 3.c)
            return arythmetic_rec(_left, _equals, _base, row + 1, col,
                                  letterDigit, digitLetter,
                                  summ, _first_letters)

        char = curr_row[col]

        if char not in letterDigit:
            # 3.b)
            return new_char_equation(char, _left, _equals, _base, col, row,
                                     letterDigit, digitLetter,
                                     summ, _first_letters)

        # if char in letterDigit:
        # 3.a)
        digit = letterDigit[char]

        if row_size - 1 == col and digit == 0:
            return None

        res = arythmetic_rec(_left, _equals, _base, row + 1, col, letterDigit,
                             digitLetter, summ + digit, _first_letters)
        return res

    assert False

def rotate(word: str) -> str:
    """
    reverse word
    """
    return "".join([word[i] for i in range(len(word) - 1, -1, -1)])


def get_first_letters(words: List[str]) -> Set[str]:
    # return {word[-1] for word in words} - yepp thi is sad story :/
    res: set[str] = set()

    for word in words:
        if len(word) > 1:  # in this case it could be just 0...
            res.add(word[-1])

    return res


def is_scam(words, result):
    scam = set(words)
    scam.add(result)
    return len(scam) == 1 and len(scam.pop()) == 1


def solve(words: List[str], result: str, base=10) -> Optional[Dict[str, int]]:
    """
    reversing all words because we want work with them from the back, when we
    rotate them we can index them normally and
    the code will be nicer and more readable
    also we want to remember first letters cause there cannot be 0
    """
    if is_scam(words, result):
        return {}

    lefts = [rotate(word) for word in words]
    right = rotate(result)

    if len(right) < max([len(x) for x in lefts]):
        return None

    first_letters: Set[str] = get_first_letters(lefts)
    first_letters.add(right[-1])

    digitLetter: Dict[int, str] = {}
    letterDigit: Dict[str, int] = {}

    return arythmetic_rec(lefts, right, base, 0, 0,
                          letterDigit, digitLetter, 0, first_letters)
