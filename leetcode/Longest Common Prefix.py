class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        a = sorted(strs, key=lambda x: len(x))
        result = ''
        length = len(a[0])
        idx = 0
        for i in range(length):
            temp = a[0][i]
            print('temp: ', temp)
            for j in range(len(a)):
                if temp != a[j][i]:
                    return result
            else:
                idx += 1
                result += temp
        return result
            

            


            
