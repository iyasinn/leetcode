class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {

        for (int i = digits.size() - 1; i >= 0; i--){
            digits[i]++;
            if (digits[i] == 10){ digits[i] = 0; }
            else { return digits;}
        }

        digits[0] = 1;
        digits.push_back(0);
        return digits; 
    }
};