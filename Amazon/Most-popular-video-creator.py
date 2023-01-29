from collections import defaultdict
def mostPopularCreator(self, creators: list[str], ids: list[str], views: list[int]) -> list[list[str]]:
        tot, vid = defaultdict(int), defaultdict(list)
        for c, i, v in zip(creators, ids, views):
            tot[c] += v  
            vid[c].append((-v,i))
        m = max(tot.values())
        return [[c,min(v)[1]] for c, v in vid.items() if tot[c] == m]