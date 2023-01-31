from collections import Counter
def topKFrequent(words: list[str], k: int) -> list[str]:
        d1=Counter(words)
        pairs = sorted(d1.items(), key = lambda p: (-p[1], p[0]))
        return [word for word, _ in pairs[0:k]]