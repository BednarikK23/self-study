package leetCode
// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/1034026410/


func twoSum(numbers []int, target int) []int {
    l, r := 0, (len(numbers) - 1)
    for l < r {
        s := numbers[l] + numbers[r]
        if s == target {
            return []int{l + 1, r + 1}
        }
        if s < target {
            l++
        } else {
            r--
        }
    }
    return []int{0, 0}
}
