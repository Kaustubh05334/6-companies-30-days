def longestPrefix(s: str) -> str:
    string = ""
    for i in range(len(s)):
        if s[:i] == s[len(s)-i:len(s)]:
            string =s[:i]
    return string