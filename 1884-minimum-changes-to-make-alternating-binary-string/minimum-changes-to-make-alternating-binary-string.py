def biconditional(a, b, size):
    bitmask = (1 << size) - 1
    result = bin((a ^ b) ^ bitmask)[2:]
    result = ('0' * (size - len(result))) + result
    return result


class Solution:
    def minOperations(self, s: str) -> int:

        number = int(s, base=2)
        num_ones = ceil(len(s) / 2)
        start_one = (pow(4, num_ones) - 1) // 3
        num_ones += -1 if len(s) % 2 == 1 else 0
        start_zero = 2 * ((pow(4, num_ones) - 1) // 3)

        diff_zero = biconditional(number, start_one, len(s))
        diff_one = biconditional(number, start_zero, len(s))

        return min(diff_zero.count('0'), diff_one.count('0')) 