"""
givens

generating fractions: O(n^2)
"""


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:

        pq = []
        for i in range(len(arr) - 1): 
    
            heapq.heappush(pq, (arr[i] / arr[-1], i, len(arr) - 1))
        

        counter = 0
       
        while len(pq) > 0: 

            val, n, d = pq[0]
            heapq.heappop(pq)
            counter += 1

            if counter == k:
                return [arr[n], arr[d]]
            if n != d: 
                d -= 1
                heapq.heappush(pq, (arr[n] / arr[d], n, d))

        return []




    




# class Solution:
#     def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
#         outputs = []
#         for i in range(len(arr)): 
#             for j in range(i + 1, len(arr)): 
#                 outputs.append([arr[i], arr[j]])
#         outputs.sort(key=lambda x: x[0] / x[1])
#         return outputs[k - 1]

      



