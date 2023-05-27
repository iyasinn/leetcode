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

    inline int maxArea(vector<int>& h){
        
        // Moving the smaller is better because the small is the limiting factor
        // So potentially the smalelr might becom elarger
        // If we move the larger, we might still need it, since it is quite large
        // In a way, we only move something when it is the shortest, because we only want to deal with some large bar

        ios_base::sync_with_stdio(false);

        int left = 0; 
        int right = h.size() - 1;
        int bestArea = 0;

        while (left < right){

            bestArea = max(bestArea, min(h[left], h[right]) * (right - left));

            if (h[left] < h[right]){
                bestArea = max(bestArea, h[left] * (right - left));
                left++;
            }
            else{
                bestArea = max(bestArea, h[right] * (right - left));
                right--;
            }
        }

        return bestArea; 
    }
};