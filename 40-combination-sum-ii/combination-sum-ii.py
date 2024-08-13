class Solution:




    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        freq = Counter(candidates)
        items = list(set(candidates))
        curr_sum = 0 
        result = []
        curr = []
        print(len(items))
        print()


        def dfs(index):
            nonlocal result
            nonlocal curr
            nonlocal curr_sum

            if curr_sum == target: 
                result.append(curr[0::])
                return
            
            if index >= len(items) or curr_sum > target: 
                return

            val = items[index]
            
            for count in range(freq[val] + 1): 

                for i in range(count): 
                    curr.append(val)
                
                curr_sum += (val * count)
                dfs(index + 1)
                curr_sum -= (val * count)

                for i in range(count): 
                    curr.pop()
            

        dfs(0)
        return result
