class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        copy = sorted(set(arr))
        m = {copy[i]: i + 1 for i in range(len(copy))}
        return [m[val] for val in arr]
        
        for i in range(len(arr)): 
            arr[i] = m[arr[i]]
        return arr