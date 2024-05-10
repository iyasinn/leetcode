"""


"""


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        # start with brute force I suppose
        outputs = []
        for i in range(len(arr)): 
            for j in range(i + 1, len(arr)): 
                outputs.append([arr[i], arr[j]])
        outputs.sort(key=lambda x: x[0] / x[1])
        return outputs[k - 1]

      



