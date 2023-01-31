def getLastMoment(n: int, left,right) -> int:
    return max(max(left, default=0), n - min(right, default=n))
