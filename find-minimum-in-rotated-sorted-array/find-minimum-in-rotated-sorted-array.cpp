class Solution {
public:


    /*
        U
        The problem has the case where the array is essentially sorted
        However, some rotation has occured
        There are two sets in the array. The set that has gone thru some rotation
        And the set that has not gone thru a rotation, or has come back to some normal sopt
        Essentially, a set that has gone thru a rotation is now seemingly out of order
        So a large value coming before a small value
        We can use this logic to help us

        M
        Binary Search, except, we are binary searching to find the smallest number
        That is not out of order

        P

    */

    int findMin(vector<int>& nums) {

        int start = 0; 
        int end = nums.size() - 1; 
        int sol = nums[0];

        while (start <= end){
            // If we reach the sorted array
            if (nums[start] < nums[end]){
                return min(sol, nums[start]);
            }
            int mid = start + (end - start) / 2;
            sol = min(sol, nums[mid]);
             
            if (nums[mid] < nums[start]){
                end = mid - 1;  
            }
            else {
                start = mid + 1; 
            }
        }
        return sol; 
    }



};