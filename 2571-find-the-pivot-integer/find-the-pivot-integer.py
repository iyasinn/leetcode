# Exponential because iterating with size of integer
class Solution:
    def pivotInteger(self, n: int) -> int:
        l, r = 0, n + 1 
        while l < r: 
            mid = l + ((r - l) // 2)
            l_sum = mid * (mid + 1) // 2
            r_sum = ((n * (n + 1)) // 2) - (mid * (mid - 1) // 2)
            if l_sum == r_sum: 
                return mid
            if l_sum > r_sum: 
                r = mid 
            else: 
                l = mid + 1
            
        return -1



# class Solution:
#     def pivotInteger(self, n: int) -> int:
#         for p in range(1, n + 1):
#             if (p * (p + 1)) // 2 == (((n * (n + 1)) // 2) - ((p * (p - 1)) // 2)):
#                 return p 
#         return -1


