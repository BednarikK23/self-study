#include <string.h>

int strStr(char * haystack, char * needle)
{
    // https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/submissions/1027627228/
    char* p = strstr(haystack, needle);

    if (p == NULL)
        return -1;

    return (p > haystack) ? p - haystack : haystack - p;
}

int searchInsert(int* nums, int numsSize, int target)
{
    // https://leetcode.com/problems/search-insert-position/submissions/1027657820/
    int l = 0;
    int r = numsSize - 1;
    int mid;

    while (l <= r) {
        mid = l + (r - l) / 2;

        if (nums[mid] == target)
            return mid;

        if (target > nums[mid]) {
            l = mid + 1;
        } else {
            r = mid - 1;
        }
    }
    return l;
}
