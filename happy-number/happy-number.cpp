class Solution {
public:                 


    int sumSquareDigits(int n){
        int total = 0; 
        string x = to_string(n);
        for (auto i : x){
            total += ((i - '0') * (i - '0'));
        }
        return total; 
    }

    bool isHappy(int n) {
        unordered_set<int> s; 
        while (n != 1 && !s.count(n)){
            s.insert(n);
            n = sumSquareDigits(n);
        }
        return n == 1; 
    }              
};