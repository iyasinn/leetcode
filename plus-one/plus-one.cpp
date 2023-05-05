class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {

        digits.back()++;

        for (int i = digits.size() - 1; i >= 1 && digits[i] > 9; i--){
            digits[i] = 0; 
            digits[i - 1]++;
        }

        if (digits[0] > 9){
            digits.resize(digits.size() + 1, 0);
            digits[0] = 1;
        }

        return digits; 
    }
};