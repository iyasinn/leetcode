class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:

        numZeros = Counter(arr[0:len(arr) - 1]).get(0, 0)
        
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] == 0: 
                numZeros -= 1

            if i + numZeros < len(arr): 
                arr[i + numZeros] = arr[i]

            if arr[i] == 0 and i + numZeros + 1 < len(arr): 
                arr[i + numZeros + 1] = arr[i]
 
        