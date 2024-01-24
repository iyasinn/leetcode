class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:

        numZeros = Counter(arr).get(0, 0)

        for i in range(len(arr) - 1, -1, -1):
            numZeros -= (arr[i] == 0)
            if i + numZeros < len(arr): 
                arr[i + numZeros] = arr[i]
            if arr[i] == 0 and i + numZeros + 1 < len(arr): 
                arr[i + numZeros + 1] = 0
            
 
        