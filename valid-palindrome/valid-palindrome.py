class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [x.lower() for x in s if x.isalnum()]
        y = s.copy()
        y.reverse()
        return s == y



