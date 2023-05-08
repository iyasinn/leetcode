class Solution {
public:
    // int diagonalSum(vector<vector<int>>& mat) {

    //     int start = 0; 
    //     int end = mat[0].size() - 1; 
    //     int sol = 0; 

    //     for (int row = 0; row < mat.size(); row++){
    //         sol += mat[row][start];
    //         sol += mat[row][end];
    //         if (start == end){ sol -= mat[row][start]; }
    //         start++; 
    //         end--; 
    //     }

    //     return sol;
    // }

    int diagonalSum(vector<vector<int>>& mat) {

        int start = 0; 
        const int numCol = mat[0].size(); 
        int sol = 0; 

        for (int row = 0; row < mat.size(); row++){
            sol += mat[row][start] + mat[row][numCol - 1 - start];
            start++; 
        }

        if (numCol % 2 == 1){
            sol -= mat[numCol / 2][numCol / 2];
        }

        return sol;
    }

};