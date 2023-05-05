class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {

        for (int i = digits.size() - 1; i >= 0; i--){
            digits[i]++;
            if (digits[i] <= 9){ return digits; }
            digits[i] = bool(i == 0) * 10; 
        }

        if (digits[0] > 9){
            digits[0] = 1;
            digits.push_back(0);
        }

        return digits; 
    }
};