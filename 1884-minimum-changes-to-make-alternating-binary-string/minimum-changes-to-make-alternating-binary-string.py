def biconditional(a, b, size):
    bitmask = (1 << size) - 1
    result = bin((a ^ b) ^ bitmask)[2:]
    remaining_zeros = size - len(result)
    result = '0' * remaining_zeros + result
    return result


# class Solution:
#     def minOperations(self, s: str) -> int:
#         number = int(s, base=2)
#         num_ones = ceil(len(s) / 2)
#         start_with_one = (pow(4, num_ones) - 1) // 3
#         num_ones += -1 if len(s) % 2 == 1 else 0
#         start_with_zero = 2 * ((pow(4, num_ones) - 1) // 3)

#         diff_zero = biconditional(number, start_with_one, len(s))
#         diff_one = biconditional(number, start_with_zero, len(s))

#         return min(diff_zero.count('0'), diff_one.count('0')) 


class Solution:
    def minOperations(self, s: str) -> int:

        start_zero = 0
        start_one = 0

        for i in range(len(s)):
            if i % 2 == 0: 
                start_zero += (s[i] != '0')
                start_one += (s[i] != '1')
            elif i % 2 == 1: 
                start_zero += (s[i] != '1')
                start_one += (s[i] != '0')
        
        return min(start_zero, start_one)

