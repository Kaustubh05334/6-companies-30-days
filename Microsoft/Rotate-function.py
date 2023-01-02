def maxRotateFunction(self, A):
    ref = curr = sum(i * j for i,j in enumerate(A))
    sum = sum(A)
    n = len(A)
    while A:
        curr += sum - A.pop() * n
        ref = max(curr, ref)
    return ref