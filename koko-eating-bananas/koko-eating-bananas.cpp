class Solution {
public:

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



    // O(n)
    inline auto checkK(vector<int>& piles, int k, int h) -> bool {

        int hours = 0; 
        for (int i = piles.size() - 1; i >= 0; i--){
            // double val = ceil(piles[i] / k);
            // int val = (piles[i] + k - 1) / k;
            // if (val > h || hours + val > h) return false;
            hours += (piles[i] + k - 1) / k;
        }
        return hours <= h;
    }

    // O(log(2^|max|) * |piles|) = O(|max| * |piles|)
    inline int minEatingSpeed(vector<int>& piles, int h) {

        int start = 1; 
        int end = 1000000000 + 1;
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


    // int minEatingSpeed(vector<int>& piles, int h) {
    //     int n(piles.size());
    //     int lo=1, hi= 1'000'000'000;//최대 스피드;
    //     while(lo<hi){
    //         int mid= lo+(hi-lo)/2;
    //         if(eat(piles,mid)<=h){
    //             hi=mid;
    //         }else lo=mid+1;
    //     }
    //     return hi;
    // }
    // int eat(vector<int> &piles, int speed){
    //     int sum=0;
    //     for(int pile:piles){
    //         // Implicitly rounds up because we are either going to the next integer than dividing down 
    //         sum+=(pile+speed-1)/speed;
    //     }
    //     return sum;
    // }

};