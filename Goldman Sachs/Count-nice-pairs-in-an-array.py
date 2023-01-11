from collections import Counter
def countNicePairs(self, nums: list[int]) -> int:
        def rev(num):
            x= (str(num))
            return int(x[::-1])
        out =0
        diff = [i-rev(i) for i in nums]
        freq = Counter(diff)
        return sum([x*(x-1)//2 for x in freq.values()])%(10**9+7)