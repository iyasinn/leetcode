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
        int sol = numeric_limits<int>::max();

        while (start <= end){
            
            int mid = start + (end - start) / 2; 

            // In this case, we know the upper portion is out of sort
            if (nums[mid] > nums[end]){
                start = mid + 1; 
            }
            // Here, it is in order, so we check the lower half of it now
            else if (nums[mid] <= nums[end]){
                sol = min(sol, nums[mid]);
                end = mid - 1; 
            }
            else {
                return nums[mid];
            }
        }
        return sol; 
    }



};