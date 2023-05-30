// class Solution {
// public:
//     vector<int> getConcatenation(vector<int>& nums) {
//         vector<int> ans(nums.size() * 2);
//         for (int i = 0; i < nums.size(); i++){
//             ans[i] = ans[nums.size() + i] = nums[i];
//         }
//         return ans; 
//     }
// };


class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
      
      vector<int> v;
      copy(nums.begin(),nums.end(), back_inserter(v));
      
      vector<int> store;
      
      for(int i = 0 ; i < v.size(); i++)
      {
         int data = v[i];
         store.push_back(data);
      }
      
      for(int i = 0 ; i < v.size(); i++)
      {
         int data = v[i];
         store.push_back(data);
      }
      
      
      return store;
    }
};