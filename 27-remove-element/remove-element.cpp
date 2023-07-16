class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int size = nums.size(); 
        for (int i = 0; i < size; i++){
            if (nums[i] == val){
                swap(nums[i], nums[--size]);
                i--; 
            }
        }
        return size;
    }
};