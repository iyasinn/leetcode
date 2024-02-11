"""

We had an O(n^3) solution
So we can now work with an O(n^2) solution 


"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0 
        for i, num in enumerate(s): 
            start = i - 1 
            end = i + 1
            count += 1

            while start >= 0 and end < len(s) and s[start] == s[end]: 
                count += 1
                start -= 1
                end += 1

            start = i
            end = i + 1 
            while start >= 0 and end < len(s) and s[start] == s[end]: 
                count += 1
                start -= 1
                end += 1

        return count 


# Simple iteration approach
# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         count = 0 
#         for i, num in enumerate(s): 
#             start = i - 1 
#             end = i + 1
#             count += 1

#             while start >= 0 and end < len(s) and s[start] == s[end]: 
#                 count += 1
#                 start -= 1
#                 end += 1

#             start = i
#             end = i + 1 
#             while start >= 0 and end < len(s) and s[start] == s[end]: 
#                 count += 1
#                 start -= 1
#                 end += 1

#         return count
            
                

        
    
