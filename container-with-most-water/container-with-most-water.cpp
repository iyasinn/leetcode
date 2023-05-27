class Solution {
public:

    // O(n^2)
    // int maxArea(vector<int>& height) {

    //     int best = 0; 

    //     for (int i = 0; i < height.size(); i++){
    //         for (int j = i + 1; j < height.size(); j++){
    //             best = max(best, min(height[i], height[j]) * (j - i));
    //         }
    //     }
        
    //     return best; 
    // }

    // Sorting method

    int maxArea(vector<int>& h){

        int left = 0; 
        int right = h.size() - 1;
        int bestArea = 0;

        while (left < right){

            bestArea = max(bestArea, min(h[left], h[right]) * (right - left));

            if (h[left] < h[right]){
                left++;
            }
            else{
                right--;
            }
        }

        return bestArea; 
    }
};