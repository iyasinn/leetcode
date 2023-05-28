// class KthLargest {

// public:

//     // Very similar to median 
//     KthLargest(int kIn, vector<int>& nums) {
//         k = kIn; 
//         for (int val: nums){
//             add(val);
//         }
//     }
    
//     int add(int val) {
        
//         topK.push(val);

//         if (topK.size() > k){
//             bottom.push(topK.top());
//             topK.pop();
//         }

//         return topK.top();
//     }

// private: 

//     priority_queue<int, vector<int>, less<int>> bottom; 
//     priority_queue<int, vector<int>, greater<int>> topK;

//     int k = 0; 
// };


class KthLargest {

public:

    // Very similar to median 
    KthLargest(int kIn, vector<int>& nums) {
        k = kIn; 
        for (int val: nums){
            add(val);
        }
    }
    
    int add(int val) {
        
        topK.push(val);
        if (topK.size() > k){
            topK.pop();
        }
        
        return topK.top();
    }

private: 

    priority_queue<int, vector<int>, greater<int>> topK;

    int k = 0; 
};


/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */