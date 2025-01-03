"""
This seems like brute force
n seems relatively small 

choose a pi

it seems we can optimize too 

n = 2

We first need to find all orderings of ps 
and then d comes after each element


n = 2 

p, p
so one d comes after one p

so how mnay ways to order n p's? 

a, b, c

n!


"""
class Solution:
    def countOrders(self, n: int) -> int:
        if n == 1:
            return 1

        mod = (10**9) + 7

        # _ a _ b _ c _ : the underscores are spots 
        prev_empty_spots = ((2 * n) - 1) 

        # find spots to insert for p_n, d_n
        spots_to_insert = ((prev_empty_spots * (prev_empty_spots + 1))) // 2 
        
        return (spots_to_insert * self.countOrders(n - 1)) % mod




       