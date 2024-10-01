#include <numeric> 

bool valid_solution(vector<int>& weights, int days, int capacity){
    int curr_day = 0, curr_capacity = 0; 
    for (int i = 0; i < weights.size(); i++){
        if (weights[i] > capacity){ return false; }
        if (curr_capacity + weights[i] > capacity){ curr_day += 1; curr_capacity = 0; }
        curr_capacity += weights[i]; 
    }
    curr_day += 1; 
    return curr_day <= days; 
}

class Solution {
public:
    int shipWithinDays(vector<int>& weights, int days) {

        int left = 0, right = 1e9; 

        while (left < right){
            int mid = (left + right) / 2; 
            if (valid_solution(weights, days, mid)){
                right = mid; 
            }
            else{
                left = mid + 1; 
            }
        }

        return right; 
    }
};