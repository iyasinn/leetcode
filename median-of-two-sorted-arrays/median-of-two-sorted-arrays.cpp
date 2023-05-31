class Solution {
public:


    // bool validMedian(vector<int>& n1, vector<int>& n2, int median){ 
    //     int left = 0; 
    //     int right = 0; 
    //     return true; 
    // }

    double findMedianSortedArrays(vector<int>& n1, vector<int>& n2) {
        
        int totalSize = n1.size() + n2.size(); 
        int left = -1; 
        
        // These are the next medians to consider in that list
        int i1 = 0; 
        int i2 = 0; 
        double median = 0;
   
        while (left < ((totalSize - 1) / 2)){
            // at the max we should say at the last index of where we wnat to include

            int add = 0; 
            
            if (i1 < n1.size() && i2 < n2.size()){ 
               median = (n1[i1] < n2[i2]) ? n1[i1++] : n2[i2++];
            }
            else if (i1 < n1.size()){
                median = n1[i1++];
            }
            else if (i2 < n2.size()){
                median = n2[i2++];
            }

            left++;
        }

        if (totalSize % 2 == 0){
            int curr = std::numeric_limits<int>::max(); 
            if (i1 < n1.size()) curr = min(curr, n1[i1]);
            if (i2 < n2.size()) curr = min(curr, n2[i2]);
            median = (median + curr) / 2.0;
        }
    
        return median; 
    }
};