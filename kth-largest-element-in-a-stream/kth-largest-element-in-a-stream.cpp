class KthLargest {

public:
    KthLargest(int kIn, vector<int>& nums) {
        k = kIn; 
        for (int val: nums){
            add(val);
        }
    }
    
    int add(int val) {
        
        topK.push(val);

        if (topK.size() > k){
            bottom.push(topK.top());
            topK.pop();
        }

        count++;
        return topK.top();
    }

private: 

    priority_queue<int, vector<int>, less<int>> bottom; 
    priority_queue<int, vector<int>, greater<int>> topK;

    int k = 0; 
    int count = 0;
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */