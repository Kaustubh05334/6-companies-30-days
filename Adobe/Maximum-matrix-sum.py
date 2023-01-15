def maxMatrixSum(matrix) -> int:
        n = len(matrix)
        minnum = float('inf')
        count = 0
        total = 0

        for i in range(n):
            for j in range(n):
                if matrix[i][j] < 0:
                    count += 1
                total += abs(matrix[i][j])
                minnum = min(minnum, abs(matrix[i][j]))
        if count % 2 == 0:
            return total
        return total - 2 * (minnum)