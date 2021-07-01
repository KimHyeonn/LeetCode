class Solution:
    def intToRoman(self, num: int) -> str:
        # 1<= num <=3999
        s = ''
        n = 1000
        if num//n >= 1:
            s += (num//n) * 'M'
            num -= n * (num//n)
            n /= 10
        else:
            n /= 10
        n = int(n)
            
        if num - 900 >= 0:
            s += 'CM'
            num -= 900
        elif num - 500 >= 0:
            s += 'D'
            num -= 500
        elif num - 400 >= 0:
            s += 'CD'
            num -= 400
        
        if num // n >= 1:
            s += (num // n) * 'C'
            num -= n * (num//n)
            n /= 10
        else:
            n /= 10
        n = int(n)
        
        if num - 90 >= 0:
            s += 'XC'
            num -= 90
        elif num - 50 >= 0:
            s += 'L'
            num -= 50
        elif num - 40 >= 0:
            s += 'XL'
            num -= 40
        
        if num // n >= 1:
            s += (num // n) * 'X'
            num -= n * (num // n)
            n /= 10
        else:
            n /= 10
        n = int(n)
            
        if num - 9 >= 0:
            s += 'IX'
            num -= 9
        elif num - 5 >= 0:
            s += 'V'
            num -= 5
        elif num - 4 >= 0:
            s += 'IV'
            num -= 4
        
        if num // n >= 1:
            s += num * 'I'
            num -= num
            
        return s