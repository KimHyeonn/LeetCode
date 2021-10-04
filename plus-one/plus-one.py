class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = 0

        for i in range(len(digits)):
            a += digits[-(i+1)]*10**i

        a += 1

        b = str(a)
        c = []
        for i in range(len(b)):
            c.append(b[i])
        return c
