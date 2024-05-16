
/*

0:00
As we add queens, we have questions to consider
Is the queen being attacked in a spot? 

Assume we place a queen in a spot. We shoud technically know which diagonal and which spot we 
can place it in 

That is to say
If we place a queen in spot 2 on row 1, then thare are n diagonals it can attack 
and 1 row and 1 column 
we can tag these rows, columns, and diagonals 

We could also search for every queen we put on
Let's try doing this first and see what happens 
Given teh solution space is pretty small 


*/


class Solution {
public:

    vector<string> curr; 
    vector<vector<string>> solution;     
    
    // vector<int> marked_row; 
    // vector<int> marked_col; 
    // vector<int> left_dig; 
    // vector<int> right_dig;

    bool valid_placement(int row, int col){

        for (int i = 0; i < curr.size(); i++){
            if (curr[row][i] == 'Q') return false; 
            if (curr[i][col] == 'Q') return false; 
        }

        int lcol = col; 
        int rcol = col; 
        while (row >= 0){
            if (lcol >= 0 && curr[row][lcol] == 'Q') return false; 
            if (rcol < curr.size() && curr[row][rcol] == 'Q') return false; 
            lcol -= 1; 
            rcol += 1; 
            row -= 1; 
        }
        return true; 
    }


    void search(int row){
        if (row == curr.size()){
            solution.push_back(curr);
            return;
        }


        for (int col = 0; col < curr.size(); col += 1){

            if (!valid_placement(row, col)) continue; 

            curr[row][col] = 'Q';
            search(row + 1); 
            curr[row][col] = '.';
        }

    }

    vector<vector<string>> solveNQueens(int n) {

        curr = vector<string>(n, string(n, '.'));

        search(0);
        return solution; 
    }
};





