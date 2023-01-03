def numberOfSubstrings(s: str) -> int:
        result = 0
        hashmap = {'a': -1, 'b': -1, 'c': -1}
        for i, c in enumerate(s):
            hashmap[c] = i
            result += 1 + min(hashmap.values())

        return result