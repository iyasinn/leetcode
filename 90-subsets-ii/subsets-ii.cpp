class Solution {
public:

    map<int, int> freq;
    vector<int> input; 

    vector<int> curr; 
    vector<vector<int>> solution; 


    void search(int i){

        if (i == input.size()){
            solution.push_back(curr); 
            return;
        }

        search(i + 1);

        for (int j = 0; j < freq[input[i]]; j += 1){
            curr.push_back(input[i]);
            search(i + 1);
        }

        for (int j = 0; j < freq[input[i]]; j += 1){
            curr.pop_back();
        }

    }


    vector<vector<int>> subsetsWithDup(vector<int>& nums) {

        for (int n : nums) freq[n] += 1;
        std::set<int> unique(nums.begin(), nums.end()); 
        input = vector<int>(unique.begin(), unique.end());

        search(0);
        return solution;
    }
};