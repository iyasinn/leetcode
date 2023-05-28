class Solution {
public:


    int best(vector<int>& piles, int start, int end, vector<vector<vector<int>>>& memo){

        if (start >= piles.size() || end < 0){
            return 0; 
        }

        bool aliceTurn = ((start - end + 1) % 2) == 0;

        if (memo[aliceTurn][start][end] != -1){
            return memo[aliceTurn][start][end];
        }

        int choseS = best(piles, start + 1, end, memo);
        int choseE = best(piles, start, end - 1, memo);

        if (aliceTurn){
            choseS += piles[start];
            choseE += piles[end];
        }
        else{
            choseS -= piles[start];
            choseE -= piles[end];
        }

        return memo[aliceTurn][start][end] = max(choseS, choseE);
    }

    bool stoneGame(vector<int>& piles) {
        vector<vector<vector<int>>> memo(2, vector<vector<int>>(piles.size(), vector<int>(piles.size(), -1)));
        int aliceMax = best(piles, 0, piles.size() - 1, memo);
        return aliceMax > 0; 
    }
};