class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        
        shortest = min(strs, key = len)
        for i, a in enumerate(shortest):
            for b in strs:
                if b[i] != a:
                    return shortest[:i]
        return shortest