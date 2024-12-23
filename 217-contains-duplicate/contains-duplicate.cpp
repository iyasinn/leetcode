// Contains duplicates 
// hold up I’ll come to ur room
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> set; // int name

        

        for (int i = 0; i < nums.size(); i++) {

            // cout << "Looking for element: " << nums[i] << endl;

            if (!set.count(nums[i])){
                // cout << "Inserting " << nums[i] << " into the set " << endl;
                set.insert(nums[i]);
            }
            else {
                // cout << "Found " << nums[i] << " twice already" << endl;
                return true;
            }
        }

        return false;
    }
};