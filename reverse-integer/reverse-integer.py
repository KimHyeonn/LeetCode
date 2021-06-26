class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            a = str(x)[::-1]
            if int(a) in range(0, 2**31 - 1):
                return int(a)
            else:
                return 0
        elif x < 0:
            a = str(x)[1:][::-1]
            if int(a) in range(0, 2**31):
                return int('-'+a)
            else:
                return 0
            