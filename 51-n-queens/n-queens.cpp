
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

    int mrow = 0; 
    int mcol = 1; 
    int mLdig = 2; 
    int mRdig = 3;  

    int dig_offset; 

    // vector<bool> markrow; 
    // vector<bool> markcol; 
    // vector<bool> markleftdig; 
    // vector<bool> markrightdig;

    vector<vector<bool>> marks; 
  

    bool valid_placement(int row, int col){
        int left_dig = row - col + dig_offset;
        int right_dig = row - (curr.size() - 1 - col) + dig_offset;
        printf("%d %d %d %d", row, col, left_dig, right_dig);
        return !(marks[mrow][row] || marks[mcol][col] 
                || marks[mLdig][left_dig] || marks[mRdig][right_dig]);
    }

    void flip_mark(int row, int col){
        marks[mrow][row] = !marks[mrow][row];
        marks[mcol][col] = !marks[mcol][col];
        int left_dig = row - col + dig_offset;
        int right_dig = row - (curr.size() - 1 - col) + dig_offset;
        marks[mLdig][left_dig] = !marks[mLdig][left_dig];
        marks[mRdig][right_dig] = !marks[mRdig][right_dig];
    }

    void search(int row){
        if (row == curr.size()){
            solution.push_back(curr);
            return;
        }

        for (int col = 0; col < curr.size(); col += 1){
            if (!valid_placement(row, col)) continue; 
            curr[row][col] = 'Q';
            flip_mark(row, col); 
            search(row + 1); 
            curr[row][col] = '.';
            flip_mark(row, col);
        }
    }

    vector<vector<string>> solveNQueens(int n) {
        curr = vector<string>(n, string(n, '.'));

        dig_offset  = n - 1; 
        marks = vector<vector<bool>>(4, vector<bool>(n + dig_offset, false));
        search(0);
        return solution; 
    }
};





