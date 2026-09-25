class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""

        for string in strs:
            code += str(len(string)) + "%" + string
        
        print(code)
        return code

    def decode(self, s: str) -> List[str]:
        i = 0
        strs = []

        while i < len(s):
            j = i

            while s[j] != '%':
                j += 1

            sLen = int(s[i:j])

            j += 1
            
            strs.append(s[j:sLen+j])

            i = j + sLen
        
        return strs
            
            
