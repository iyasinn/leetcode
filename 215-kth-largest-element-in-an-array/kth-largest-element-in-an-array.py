class Solution:
    # Sorting as an operation takes n log n time 
    # We could potentially use a priority queue 
    # This would take O(n) time to create the priority queue 
    # Then it would take k - 1 removal operations to get the kth largest element. Each removal is O(log(k)), note that priority queues are not sorted
    # O(k log(k)) to do this 
    # A bucket sort could be even better.
    # Max amount of frequency is n
    # Find frequency in O(n). Then put in buckets 
    # Then go backwards in O(k) time to find the kth largest element
    # We will do both implementations
    # Actually bucket sort will not work because we need the buckets to be the value of the elements rather than frequency, and that cause sissus because

    def findKthLargest1(self, nums: List[int], k: int) -> int:

        maxHeap = [-1 * element for element in nums]
        # This is a min heap, we need a max heap using heapify
        # Inverting to get a max heap 
        # heapq.heapify(maxHeap)

        for _ in range(k - 1):
            heapq.heappop(maxHeap)
        
        return heapq.heappop(maxHeap) * -1

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        print(nums)
        maxVal = nums[0]
        minVal = nums[0]

        for n in nums: 
            maxVal = max(maxVal, n)
            minVal = min(minVal, n)

        size = maxVal - minVal 
        bucket = [0 for _ in range(size + 1)]
        
        for num in nums: 
            bucket[num - minVal] += 1 

        # print(bucket)

        for i in range(len(bucket) - 1, -1, -1):
            if (bucket[i] >= k):
                return i + minVal
            k -= bucket[i]
        
        return -1

        # Sorting is faster in python
    # Quick select is quick sort but we select half the array
    # Average case is O(n), worst is O(n^2)
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # [l, r] inclusive
        def quickSelect(l, r): 
            
            p = l
            pivot = nums[r]
            
            # Quickselect is just a greedy selection algorithm
            for i in range(l, r): 
                if (nums[i] <= pivot): 
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            # p is at a point where it is no longer <= 1, if it was, we would have continue
            nums[p], nums[r] = nums[r], nums[p]
            if (p < k): 
                return quickSelect(p + 1, r)
            elif (p > k):
                return quickSelect(l, p - 1)
            return nums[p]

        l = 0 
        r = len(nums) - 1

        # When dealing with positions quesitons, look for iconverting ranks into indexes
        k = len(nums) - k 
        return quickSelect(0, len(nums) - 1)