class Solution:
    def romanToInt(self, s: str) -> int:
        converter = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        result = 0
        flag = False
        for i in range(len(s)-1, -1, -1):
            if (s[i] == 'V' or s[i] == "X") and i != 0 and not flag:
                if s[i-1] == 'I':
                    result += converter[s[i]] - 1
                    flag = True
                    continue
            elif (s[i] == 'L' or s[i] =='C') and i != 0 and not flag:
                if s[i-1] == 'X':
                    result += converter[s[i]] - 10
                    flag = True
                    continue
            elif (s[i] == 'D' or s[i] == 'M') and i != 0 and not flag:
                if s[i-1] == 'C':
                    result += converter[s[i]] - 100
                    flag = True
                    continue
            if flag:
                flag = False
                continue
            result += converter[s[i]]
        return result
                    
                    

