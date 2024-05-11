"""
givens

generating fractions: O(n^2)
"""


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:

        pq = []
        for i in range(len(arr) - 1): 
            heapq.heappush(pq, (arr[i] / arr[-1], i, len(arr) - 1))

        for i in range(k - 1): 
            _, n, d = pq[0]
            heapq.heappop(pq)
            if n == d:
                continue
            d -= 1
            heapq.heappush(pq, (arr[n] / arr[d], n, d))

        return [arr[pq[0][1]], arr[pq[0][2]]]




    




# class Solution:
#     def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
#         outputs = []
#         for i in range(len(arr)): 
#             for j in range(i + 1, len(arr)): 
#                 outputs.append([arr[i], arr[j]])
#         outputs.sort(key=lambda x: x[0] / x[1])
#         return outputs[k - 1]

      



