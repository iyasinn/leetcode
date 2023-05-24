class Solution {
public:


    // O(n)
    auto checkK(vector<int>& piles, double k, int h) -> bool {
        long int hours = 0; 
        for (auto x : piles){
            if (ceil(x / k) > h){ return false; }
            hours += ceil(x / k);
        }
        return hours <= h; 

    }

    // O(2^|max| * |piles|)
    // int minEatingSpeed(vector<int>& piles, int h) {

    //     int currMax = *max_element(piles.begin(), piles.end());

    //     for (int k = 1; k <= currMax; k++){
    //         if (checkK(piles, k, h)){
    //             return k; 
    //         }
    //     }

    //     return -1; 
    //     return currMax; 
    // }


    // O(log(2^|max|) * |piles|) = O(|max| * |piles|)
    int minEatingSpeed(vector<int>& piles, int h) {

        int start = 0; 
        int end = *max_element(piles.begin(), piles.end()) + 1;
        int best = 0; 

        while (start < end){
            int mid = start + ((end - start) / 2); 

            if (checkK(piles, mid, h)){
                best = mid; 
                end = mid; 
            }
            else{
                start = mid + 1; 
            }
        }

        return best;
    }
};