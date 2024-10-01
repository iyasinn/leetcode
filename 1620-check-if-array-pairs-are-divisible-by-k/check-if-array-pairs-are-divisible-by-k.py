"""

let (a + b) % k == 0 

(a + b) / k = q

Given an integer, we know there is exactly one other element that makes it divisible by k 

So for each n element, we could just search for other in O(n^2)

Or, we can sort array, then search for it in O(nlogn + nlogn) = O(nlogn)

We could do something else too. We could create a multiset, aka a hashmap to counters
And then we can simply see if an element exists as needed

(a + b) % k == 0 

so if a / k -> We simply see what is the remainder
And thats how much we need to add to a 
2/4. -> remainder is 2, thats how much we need to add on 

a % k -> [0, k]
And thats the range of the number that we need to add to a so it gtes into the congruence set and is divisible by k


"""



class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:


        new = [0] * (k)
        for i in range(len(arr)): 
            modulo = arr[i] % k
            if modulo < 0: 
                modulo += k 
            new[modulo] += 1

        for val in range((len(new) // 2 + 1)):
            other = 0 if val == 0 else k - val
            if val == other and new[val] % 2 != 0: 
                return False
            elif new[val] != new[other]: 
                return False

        return True


        