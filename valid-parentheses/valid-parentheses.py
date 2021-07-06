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
            
#class Solution:
#    # @return a boolean
#    def isValid(self, s):
#        stack = []
#        dict = {"]":"[", "}":"{", ")":"("}
#        for char in s:
#            if char in dict.values():
#                stack.append(char)
#            elif char in dict.keys():
#                if stack == [] or dict[char] != stack.pop():
#                    return False
#            else:
#                return False
#        return stack == []
