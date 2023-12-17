class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: 
            return '1'

        data = self.countAndSay(n - 1)


        count = 1
        num = data[0]

        output = ""

        for i in range(1, len(data)):  
            if data[i] != num: 
                output += str(count) + str(num)
                count = 1
                num = data[i]
            else: 
                count += 1
            
        output += str(count) + str(num)

        return output



            

        

        
