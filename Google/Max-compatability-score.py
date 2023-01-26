from functools import cache
def maxCompatibilitySum(students, mentors) -> int:
        m = len(students)
        
        score = [[0]*m for _ in range(m)]
        for i in range(m): 
            for j in range(m): 
                score[i][j] = sum(x == y for x, y in zip(students[i], mentors[j]))
        
        @cache 
        def fn(mask, j): 
            """Return max score of assigning students in mask to first j mentors."""
            ans = 0 
            for i in range(m): 
                if not mask & (1<<i): 
                    ans = max(ans, fn(mask^(1<<i), j-1) + score[i][j])
            return ans 
        
        return fn(1<<m, m-1)