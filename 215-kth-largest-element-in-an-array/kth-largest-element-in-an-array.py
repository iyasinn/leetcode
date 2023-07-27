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
    def findKthLargest(self, nums: List[int], k: int) -> int:

        maxHeap = [-1 * element for element in nums]
        # This is a min heap, we need a max heap using heapify
        # Inverting to get a max heap 
        heapq.heapify(maxHeap)

        for _ in range(k - 1):
            heapq.heappop(maxHeap)
        
        return heapq.heappop(maxHeap) * -1

