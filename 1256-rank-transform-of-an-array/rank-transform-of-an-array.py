class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        copy = list(set(arr))
        copy.sort()
        m = {copy[i]: i + 1 for i in range(len(copy))}
        
        for i in range(len(arr)): 
            arr[i] = m[arr[i]]

        return arr