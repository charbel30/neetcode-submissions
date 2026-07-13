class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = {}
        for i in range(len(s)):
            count[s[i]] = 1 + count.get(s[i], 0)
        res = []
        for c in order:
            if c in count:
                res.extend([c] * count[c] )
                del count[c]
        for char, value in count.items():
            res.extend([char] * value)
            
        return "".join(res)

