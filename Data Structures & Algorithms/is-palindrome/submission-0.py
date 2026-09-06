class Solution:
    def isPalindrome(self, s: str) -> bool:
        edit = ""
        for w in s:
            if w.isalnum():
                edit += w.lower()
        
        n = len(edit)

        first = ""
        second = ""
        if n % 2 == 0:
            first += edit[:n//2]
            second += edit[n//2:]
        else:
            first += edit[:n//2 + 1]
            second += edit[n//2:]

        print(first, second)
        
        return first == second[::-1]