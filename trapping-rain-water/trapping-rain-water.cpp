class Solution {
public:



    int trap(vector<int>& h) {

        int total = 0;
        int left = 0; 
        int right = h.size() - 1; 

        int leftMax = h[left];
        int rightMax = h[right];

        while (left < right){

            if (leftMax <= rightMax){
                total += leftMax - h[left];
                left++; 
                leftMax = max(leftMax, h[left]);
            }
            else{
                total += rightMax - h[right];
                right--; 
                rightMax = max(rightMax, h[right]);
            }
        }

        return total;         
    }
};