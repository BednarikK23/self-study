package leetCode

// https://leetcode.com/problems/minimum-penalty-for-a-shop/submissions/1034995292/

func bestClosingTime(customers string) int {
    y, n := 0, 0
    for i := 0; i < len(customers); i++ {
        if customers[i] == 'Y'{
            y++
        } else {
            n++
        }
    }

    close_time, best_close := 0, y - n
    for i, c := range customers {
        if c == 'Y' {
            y--
        } else {
            n--
        }

        curr := y - n
        if curr < best_close {
            best_close = curr
            close_time = i + 1
        }
    }

    return close_time
}
