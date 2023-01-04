from sortedcontainers import SortedList
def numberOfPairs(nums1, nums2, diff: int) -> int:
    sl, ans = SortedList(), 0
    for num1, num2 in zip(nums1, nums2):
        ans += sl.bisect_right(num1 - num2 + diff)
        sl.add(num1 - num2)
    return ans