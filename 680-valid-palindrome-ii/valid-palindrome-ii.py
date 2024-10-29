
def checkPalindrome(s):
    return s == s[::-1]

class Solution:


    def validPalindrome(self, s: str) -> bool:
            
        s = list(s)

        l = 0
        r = len(s) - 1

        while l <= r:
            # mistamtch, so now choose to delete 1 and see if palindrome
            if s[l] != s[r]:
                return checkPalindrome(s[l:r]) or checkPalindrome(s[l+1:r+1])

            r -= 1
            l += 1

        return True


        