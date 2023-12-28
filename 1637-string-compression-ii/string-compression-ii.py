"""
0:00
Reading
Run-encoding compressoin takes a word and makes something like:
aaa = a3 and ccc as c3
We don't make a = a1, instead, a = a

Need to delete at most k characters from s such that the encoded version of s is minimum

Could we choose two characters to delete and then calculate minimum? 
O(n^3), n^2 for every pair, n for run-encoded vesion

2:33
Observation: a10 -> remove one a -> a9
The length decreased by 1
a2 -> remove one letter -> a 

So the length decreases when we remove enough letters to make the count go from 10^n to 10^(n-1) or 1

But how do we determine what to delete? 

3:46
For each character, we need minimum distances to get to the next smallest integer shift
We need to prioritize

aaa b ccc d 
a3  b  c3 d
3    1  3   1    numRemovals

We could get to the next vailable number to remove, but then we need to cvonsider the next amoutn after
This would be an O(slogs * k) algorithm 

a b aaa -> aba3
Removnig b gives -> a4 -> So it knocked out two characters

---

We can consider then that can we break this problem down 
a3ba3 -> We can choose to break down a3 or not. How far we break it down can also matter. 
-> After breaking it down we can also pass in what is left over from breaking it down -> 
a3ba3 -> a3 to a -> a3ba -> Go back one a3ba -> remove one from b -> a3a -> a4


We can simply say that for each thing

a2 b a2
WE can stgart at a2, remove it




T(n, k) = min(
    for i in [0, k]
    T(n - 1, 

"""





def dp(data, i, k, prev):

    if i < 0: 
        return 0

    part = data[i]



class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        dp = [[9999] * 110 for _ in range(110)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(0, k + 1):
                cnt, del_ = 0, 0
                for l in range(i, 0, -1):
                    if s[l - 1] == s[i - 1]:
                        cnt += 1
                    else:
                        del_ += 1

                    if j - del_ >= 0:
                        dp[i][j] = min(dp[i][j], dp[l - 1][j - del_] + 1 + (3 if cnt >= 100 else 2 if cnt >= 10 else 1 if cnt >= 2 else 0))

                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])

        return dp[n][k]


# class Solution:
#     def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

#         data = [s[0]]

#         for char in s: 
#             if char != data[-1][0]: 
#                 data.append(char)
#             else: 
#                 data[-1] += char
        
#         for i in range(len(data)): 
#             if len(data[i]) > 1: 
#                 data[i] = data[i][0] + str(len(data[i]))

#         # Now we can work with this 
#         print(data)


#         return 3
        











    









    