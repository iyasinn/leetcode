class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [x.lower() for x in s if x.isalnum()]
        y = s[:]
        y.reverse()
        return s == y



