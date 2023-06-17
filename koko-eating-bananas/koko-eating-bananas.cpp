class Solution {
public:


    bool works(vector<int>& piles, int k, int h){
        double hours = 0; 
        for (int x : piles){
            hours += ceil(x * 1.0 / k);
        }
        return hours <= h; 
    }

    int minEatingSpeed(vector<int>& piles, int h) {

        int start = 1; 
        int end = *max_element(piles.begin(), piles.end()); 
        int best = end; 

        while (start <= end){

            int mid = start + (end - start) / 2;

            cout << mid << endl;

            if (works(piles, mid, h)){
                best = min(best, mid);
                end = mid - 1; 
            }
            else {
                start = mid + 1; 
            }
        }

        return best; 
    }
};