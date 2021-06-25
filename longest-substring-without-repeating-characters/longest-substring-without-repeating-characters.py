class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for i, a in enumerate(s):
            if a in used and start <= used[a]:
                start = used[a] + 1
            else:
                max_length = max(max_length, i - start + 1)
            
            used[a] = i

    
        return max_length