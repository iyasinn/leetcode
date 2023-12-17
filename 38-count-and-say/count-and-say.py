class Solution:
    def countAndSay(self, n: int) -> str:

        if n == 1: 
            return '1'

        data = self.countAndSay(n - 1)

        start = 0 
        end = 0
        curr_num = None
        output = ""

        while end < len(data): 
            if data[end] != curr_num:
                if curr_num is not None:  
                    count = str(end - start)
                    output += count + curr_num
                curr_num = data[end]
                start = end
            end += 1
        count = str(end - start)
        output += count + curr_num

        return output



            

        

        
