class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_string = " ".join(c.lower() for c in s if c.isalnum())

        return clean_string == clean_string[::-1]

