class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        else:
            while '()' in s or '{}' in s or '[]' in s:
                s = s.replace('{}','').replace('()','').replace('[]','')
                
            if s == '':
                return True
            else:
                return False