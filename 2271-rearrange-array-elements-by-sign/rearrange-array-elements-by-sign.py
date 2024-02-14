class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = [n for n in nums if n > 0]
        negatives = [n for n in nums if n < 0]
        output = []
        for i in range(len(positives)): 
            output.append(positives[i])
            output.append(negatives[i])
        return output
