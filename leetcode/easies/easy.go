package main

func climbStairs(n int) int {
	// https://leetcode.com/problems/climbing-stairs/submissions/1027783423/
	if n == 1 {
		return 1
	}

	// bottom up dp - ways to get to top for first 6: [8, 5, 3, 2, 1, 1]
	lst, pre := 1, 1

	for i := 0; i < n-1; i++ {
		tmp := lst
		lst = lst + pre
		pre = tmp
	}

	return lst
}
