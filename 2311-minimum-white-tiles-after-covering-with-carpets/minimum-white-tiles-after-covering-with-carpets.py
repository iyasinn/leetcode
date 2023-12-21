class Solution:
        
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        
        @cache
        def dp(index, numCarpets): 
            if index < 0: 
                return 0
            if floor[index] == '0':
                return dp(index - 1, numCarpets)
                
            no_place = dp(index - 1, numCarpets) + 1
            place_carpet = dp(index - carpetLen, numCarpets - 1) if numCarpets > 0 else no_place
            return min(no_place, place_carpet)

            return dp(len(floor) - 1, numCarpets)
        
        return dp(len(floor) - 1, numCarpets)