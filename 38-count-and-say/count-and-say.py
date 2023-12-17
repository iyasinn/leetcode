class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: 
            return '1'

        data = self.countAndSay(n - 1)

        start = 0 
        end = 1
        curr_num = data[0]
        output = ""

        while end < len(data): 
            if data[end] != curr_num:
                count = str(end - start)
                output += count + curr_num
                curr_num = data[end]
                start = end
            end += 1
            
        count = str(end - start)
        output += count + curr_num

        return output



            

        

        
