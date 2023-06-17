class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {

        int rowLeft = 0; 
        int rowRight = matrix.size() - 1;

        while (rowLeft <= rowRight){
            int rowMid = rowLeft + (rowRight - rowLeft) / 2; 
            cout << rowMid << endl;
            if (matrix[rowMid][0] > target){
                rowRight = rowMid - 1;
            }
            else if (matrix[rowMid].back() < target){
                rowLeft = rowMid + 1; 
            }
            else{
                return binary_search(matrix[rowMid].begin(), matrix[rowMid].end(), target);
            }
        }
        return false; 
        
    }
};