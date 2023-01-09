def maximumBobPoints( numArrows: int, aliceArrows):
        bestScore = 0
        bestBobArrows = None
        
        def backtracking(k, remainArrows, score, bobArrows):
            if k == 12:
                if score > bestScore:
                    bestScore = score
                    bestBobArrows = bobArrows[::]
                return
            
            backtracking(k+1, remainArrows, score, bobArrows)  # 
            arrowsNeeded = aliceArrows[k] + 1
            if remainArrows >= arrowsNeeded:
                old = bobArrows[k]
                bobArrows[k] = arrowsNeeded
                backtracking(k+1, remainArrows - arrowsNeeded, score + k, bobArrows)
                bobArrows[k] = old
                
        backtracking(0, numArrows, 0, [0] * 12)
        bestBobArrows[0] += numArrows - sum(bestBobArrows)
        return bestBobArrows