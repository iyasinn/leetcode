#include <algorithm>

class CustomStack {
public:
    CustomStack(int maxSize) {
        _maxSize = maxSize; 
    }
    
    void push(int x) {
        if (vec.size() != _maxSize){
            vec.push_back(x); 
        }
    }
    
    int pop() {
        if (vec.size() == 0){
            return -1; 
        }

        int top = vec.back(); 
        vec.pop_back(); 
        return top; 
    }
    
    void increment(int k, int val) {
        for (int i = 0; i < std::min(k, int(vec.size())); i++){
            vec[i] += val; 
        }
    }

private: 
    std::vector<int> vec; 
    int _maxSize; 
};

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack* obj = new CustomStack(maxSize);
 * obj->push(x);
 * int param_2 = obj->pop();
 * obj->increment(k,val);
 */