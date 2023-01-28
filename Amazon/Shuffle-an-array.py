import random
class Solution:
    def __init__(self, nums: list[int]):
        self.arr=nums
        self.real=nums[:]
    def reset(self) -> list[int]:
        return self.real
    def shuffle(self) -> list[int]:
        narr=self.arr
        n=len(narr)
        for i in range(n):
            a=random.randint(0,n-1)
            b=random.randint(0,n-1)
            narr[a],narr[b]=narr[b],narr[a]
        return narr