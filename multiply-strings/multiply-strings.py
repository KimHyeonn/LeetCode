class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        i, j = len(num1), len(num2)
        
        a = 0
        
        for k in range(0, i):
            for v in range(0, j):
                a += int(num1[::-1][k]) * int(num2[::-1][v]) * 10**(k) * 10**(v)
        
        return str(a)