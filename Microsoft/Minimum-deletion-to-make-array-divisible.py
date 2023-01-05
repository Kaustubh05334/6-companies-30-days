def minOperations(nums, numsDivide) -> int:
    visited=[]
    nums.sort()
    numsDivide = set(numsDivide)
    for num in nums:
        if num in visited:
            continue
        else:
            for nd in numsDivide:
                if nd%num ==0:
                    continue
                else:
                    break
            else:
                return nums.index(num)
            visited.append(num)
    return -1