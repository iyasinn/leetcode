class Solution:
    ''' 
        Methods for arrays 
            - Iteration
            - Binary Search / sorting
            - Two pointer
            - Sliding Window
            - Hashmap 
            - Prefix/Postfix 
            - Priority Queue
            - Sorting
            - Dynamic Programming

        Test case
        [3, 5, 7, 11] h = 8
        If we did a brute force 
        h = 1, we see it takes 26 hours
        k = 2...
        For each k check, it takes O(n) time to check because we need to check each index and see how much time it takes 
        Observation: numHours(arr, n) = O(n) 

        We can brute force in O(k) time from 1 to k
        Issue: Time complexity based on an integer is O(2^|k|) complexity

        Binary search? 
        O(log(2^|k|)) = O(|k|)
        This would lead to a final O(n * |k|) complexity, which seems quite good 

    '''


    def getHours(self, piles, k): 
        hours = 0 
        for pile in piles: 
            hours += ceil(pile / k)
        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # [start, end)
        start = 1
        end = max(piles) + 1
        best = end + 1

        while (start < end): 

            mid = (start + end) // 2
            print(mid)

            hours = self.getHours(piles, mid)
            print(hours)
            print()

            if hours <= h: 
                end = mid
                best = mid
            else: 
                start = mid + 1
        
        return best
























