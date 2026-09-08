class Solution:

    def encode(self, strs: List[str]) -> str:
        coded = ""
        for string in strs:
            coded += string
            coded += "*-*"
        
        print(coded)
        
        return coded


    def decode(self, s: str) -> List[str]:
        current_ind = 0
        prev_ind = 0
        strs = []
        while True:
            if current_ind >= len(s):
                break
            
            if s[current_ind:current_ind+3] == "*-*":
                strs.append(s[prev_ind:current_ind])
                current_ind = current_ind + 2
                prev_ind = current_ind + 1
                
                

            current_ind += 1
        
        print(strs)
        return strs



