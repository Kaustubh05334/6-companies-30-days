from collections import deque
def maxCoins(piles) -> int:
        piles.sort()
        piles = deque(piles)
        output=0
        for i in range(len(piles)//3):
            output+=piles[-2]
            piles.pop()
            piles.pop()
            piles.popleft()
        return output