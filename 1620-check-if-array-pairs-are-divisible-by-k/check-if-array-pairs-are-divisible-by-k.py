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

        for i in range(len(arr)): 
            arr[i] = arr[i] % k

        freq = Counter(arr)
        print(freq)

        for n in arr:

            if freq[n] == 0: 
                continue 

            other = k - (n % k)
            other = 0 if other == k else other

            if n == 0 and other == 0 and freq[0] >= 2: 
                continue

            freq[n] -= 1

            if other != 0 and other not in freq or freq[other] == 0:
                return False 
            freq[other] -= 1

        return True


        