class Solution {
public:
    long long maximumHappinessSum(vector<int>& happiness, int k) {
        sort(happiness.begin(), happiness.end(), std::greater<int>());
        long long total = 0; 
        for (int i = 0; i < k; i++){
            total += max(0, happiness[i] - i); 
        }
        return total; 
    }
};