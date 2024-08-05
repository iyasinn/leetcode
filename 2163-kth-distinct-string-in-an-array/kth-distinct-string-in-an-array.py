class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        freq = Counter(arr)
        result = None

        for n in arr: 
            if freq[n] == 1 and k > 0: 
                result = n
                k -= 1

        return result if k == 0 else ""
