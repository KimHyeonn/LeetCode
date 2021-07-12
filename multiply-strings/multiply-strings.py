class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        i, j = len(num1), len(num2)
        
        a = 0
        
        for k in range(1, i+1):
            for v in range(1, j+1):
                a += int(num1[-k]) * int(num2[-v]) * 10**(k-1) * 10**(v-1)
        
        return str(a)