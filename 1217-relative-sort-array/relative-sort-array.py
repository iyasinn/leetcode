
"""

arr2 are distinct
arr2 in arr1

sort such that they are in arr2 
I think we could create an indice map 
and that indice map then is our new wya of comparing values 

"""

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        pos = {arr2[i]: i for i in range(len(arr2))}
        arr1.sort(key=lambda x: (pos.get(x, 100000), x))
        return arr1

