class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int: 
        freq_recent = 0 
        curr = 0
        max_freq = 0  
        max_num = 0

        for num in arr: 
            if num == curr: 
                freq_recent += 1
            elif num != curr and max_freq < freq_recent: 
                max_freq = freq_recent 
                max_num = curr
                freq_recent = 1
                curr = num
            else: 
                freq_recent = 1
                curr = num

        if freq_recent > max_freq: 
            max_num = curr

        return max_num



        