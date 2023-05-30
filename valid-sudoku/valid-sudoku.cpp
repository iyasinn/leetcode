class Solution {
public:

    bool isValidSudoku(vector<vector<char>>& board) {   

        for (int row = 0; row < 9; row++){
            vector<int> n(11, 1);
            for (char c : board[row]){
                if (c == '.') continue; 
                if (n[c - '0'] == 0){ return false; }
                n[c - '0']--;
            }
        }

        for (int col = 0; col < 9; col++){
            vector<int> n(11, 1);
            for (int row = 0; row < 9; row++){
                if (board[row][col] == '.') continue; 
                if (n[board[row][col] - '0'] == 0){ return false; }
                n[board[row][col] - '0']--;
            }
        }

        for (int row = 0; row < 9; row += 3){
            for (int col = 0; col < 9; col += 3){
                vector<int> n(10, 1);
                for (int sRow = 0; sRow < 3; sRow++){
                    for (int sCol = 0; sCol < 3; sCol++){
                        if (board[row + sRow][col + sCol] == '.') continue; 
                        n[board[row + sRow][col + sCol] - '0']--; 
                    }
                }

                for (auto x : n){
                    if (x < 0){ return false; }
                }

            }
        }


        return true; 


    }
};