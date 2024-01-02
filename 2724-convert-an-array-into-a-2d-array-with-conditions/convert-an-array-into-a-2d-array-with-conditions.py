"""
0:00
Observation: numRows = max(frequency of a given element)

If we create a frequency map
For each row, we can iterate through the frequency map
The frequency map consists of O(m) frequencies
O(n) rows

If n = 1 type of elements, then numRows = n, so O(n) complexity
if n = distinct n elements, then numRows = 1, so O(n) complexity
Can it be O(n^2)
"""

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        numRows = 0 
        freq = {}
        for n in nums: 
            freq[n] = freq.get(n, 0) + 1
            numRows = max(numRows, freq[n])
        output = []
        for _ in range(numRows): 
            output.append([])
            for n in freq: 
                if freq[n] > 0: 
                    freq[n] -= 1
                    output[-1].append(n)
        return output