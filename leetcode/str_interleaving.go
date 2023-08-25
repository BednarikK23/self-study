package main

// https://leetcode.com/problems/interleaving-string/submissions/1031788494/

func isInterleave(s1 string, s2 string, s3 string) bool {
	l1, l2 := len(s1), len(s2)
	if l1+l2 != len(s3) {
		return false
	}

	res := make([]bool, l2+1)
	res[0] = true

	for j := 1; j <= l2; j++ {
		res[j] = res[j-1] && s2[j-1] == s3[j-1]
	}

	for i := 1; i <= l1; i++ {
		res[0] = res[0] && s1[i-1] == s3[i-1]

		for j := 1; j <= l2; j++ {
			res[j] = (res[j] && s1[i-1] == s3[i+j-1]) || (res[j-1] && s2[j-1] == s3[i+j-1])
		}
	}

	return res[l2]
}
