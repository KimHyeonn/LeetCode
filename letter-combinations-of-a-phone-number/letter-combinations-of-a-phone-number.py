class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            2 : ['a', 'b', 'c'],
            3 : ['d', 'e', 'f'],
            4 : ['g', 'h', 'i'],
            5 : ['j', 'k', 'l'],
            6 : ['m', 'n', 'o'],
            7 : ['p', 'q', 'r', 's'],
            8 : ['t', 'u', 'v'],
            9 : ['w', 'x', 'y', 'z']
        }
        ld = len(digits)
        a = []
        i , j, k, l = 0, 1, 2, 3
        if ld == 0:
            return a
        
        elif ld == 1:
            return dic.get(int(digits))
        
        elif ld == 2:
            for m in range(0, len(dic.get(int(digits[i])))):
                for n in range(0, len(dic.get(int(digits[j])))):
                    a.append(dic.get(int(digits[i]))[m] +\
                             dic.get(int(digits[j]))[n])
            return a
        
        elif ld == 3:
            for m in range(0, len(dic.get(int(digits[i])))):
                for n in range(0, len(dic.get(int(digits[j])))):
                    for o in range(0, len(dic.get(int(digits[k])))):
                        a.append(dic.get(int(digits[i]))[m] +\
                                 dic.get(int(digits[j]))[n] +\
                                 dic.get(int(digits[k]))[o])
            return a
        
        else:
            for m in range(0, len(dic.get(int(digits[i])))):
                for n in range(0, len(dic.get(int(digits[j])))):
                    for o in range(0, len(dic.get(int(digits[k])))):
                        for p in range(0, len(dic.get(int(digits[l])))):
                            a.append(dic.get(int(digits[i]))[m] +\
                                     dic.get(int(digits[j]))[n] +\
                                     dic.get(int(digits[k]))[o] +\
                                     dic.get(int(digits[l]))[p])
            return a