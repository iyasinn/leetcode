class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq = {}
        for char in tasks: 
            freq[char] = freq.get(char, 0) + 1
        
        hp = []
        for key, count in freq.items(): 
            heapq.heappush(hp, (-1 * count, key))
    
        # Observation: separate active elements in pq from cooldown elements in a queue
        cooldown = []
        time = 0

        while len(hp) > 0 or len(cooldown) > 0:

            while len(cooldown) > 0 and cooldown[0][0] <= time: 
                _, count, key = cooldown[0]
                heapq.heappush(hp, (count, key))
                cooldown.pop(0)
                            
            if len(hp) == 0: 
                time += 1
                continue
            
            count, key = heapq.heappop(hp)
            count *= -1

            if count == 0: 
                continue    
            elif count > 1:   
                cooldown.append((time + n + 1, -1 * (count - 1), key))                  

            time += 1

        return time
        

        