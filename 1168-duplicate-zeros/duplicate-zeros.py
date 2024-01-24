
"""

0:00
Think of the approach 
1, 0, 2, 3, 0, 4, 5, 0
We see 0, nothing, 
we see 5, and since we have at least one shift, we can say 5 jumps to index + shift
Everything at n - shift is going to dissapear
Unless But the shift also decreases 

When seeing a 0 we need a move
Wanna do this in O(1)
we can consider num zeros
"""

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        # So that means every word needs to be move over by 0 

        numZeros = Counter(arr).get(0, 0)

        if arr[-1] == 0: 
            numZeros -= 1
        
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] == 0: 
                numZeros -= 1

            if i + numZeros < len(arr): 
                arr[i + numZeros] = arr[i]

            if arr[i] == 0 and i + numZeros + 1 < len(arr): 
                arr[i + numZeros + 1] = arr[i]
 
        