def helper(s, seen):
	ans = 0
	if s:
		for i in range(1, len(s) + 1):
			candidate = s[:i]
			if candidate not in seen:
				seen.add(candidate)
				ans = max(ans, 1 + helper(s[i:], seen))
				seen.remove(candidate)
	return ans

def maxUniqueSplit(s: str) -> int:
	seen = set()
	return helper(s, seen)


    