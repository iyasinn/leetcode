class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        events = {}
        for birth, death in logs: 
            events[birth] = events.get(birth, 0) + 1
            events[death] = events.get(death, 0) - 1
        
        max_pop = 0
        min_year = 0
        curr_pop = 0


        for year in sorted(events.keys()): 

            curr_pop += events[year]

            if curr_pop > max_pop: 
                min_year = year
                max_pop = curr_pop
 
        return min_year
        