class MinStack {
public:
    MinStack() {  
    }
    
    void push(int val) {

        data.push_back(val);

        if (size == 0){
            minData.push_back(val);
        }
        else {
            minData.push_back(min(val, minData.back()));
        }

        size++;
    }
    
    void pop() {
        data.pop_back();
        minData.pop_back();
        size--; 
    }
    
    int top() {
        return data.back();
    }
    
    int getMin() {
        return minData.back();
    }

private: 
    vector<int> data;
    vector<int> minData;
    int size = 0; 
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */