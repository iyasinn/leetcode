class Solution {
public:
    int arraySign(vector<int>& nums) {
        int sign = 1; 
        auto it = nums.begin();
        
        while (it != nums.end() && *it != 0){
            sign = sign * (*it != 0);
            sign *= ((*it > 0) * 2 - 1);
            it++;
        }

        return (it != nums.end() && *it == 0) ? 0 : sign;
    }
};