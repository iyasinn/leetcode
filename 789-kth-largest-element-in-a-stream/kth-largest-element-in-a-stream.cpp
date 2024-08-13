class KthLargest {
public:
    KthLargest(int k, vector<int>& nums) : _k(k){
        for (int n : nums){
            upper.push(n);
        }
        while (upper.size() > k){
            upper.pop();
        }
    }
    
    int add(int val) {
        upper.push(val);

        while (upper.size() > _k){
            upper.pop();
        }
        
        return upper.top();
    }

private: 
    int _k; 
    std::priority_queue<int, std::vector<int>, std::greater<int>> upper;

};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */