class Solution:
    def romanToInt(self, s: str) -> int:
        i, val = 0, 0
        
        dic = {'I' : 1,
               'V' : 5,
               'X' : 10,
               'L' : 50,
               'C' : 100,
               'D' : 500,
               'M' : 1000}
        
        a = []
        while i < len(s):
            a.append(dic.get(s[::-1][i]))
            i += 1
        
        j, sign = 1, -1
        val += a[0]

        while j <= len(a)-1:
            if a[j-1] > a[j]:
                val += sign*a[j]
                j += 1
            else:
                val += a[j]
                j += 1
        
        return(val)

            
        return val