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
        while (true){
            s.insert(n);
            n = sumSquareDigits(n);
            if (n == 1){ return true; }
            if (s.count(n)){ break; }
        }
        return false; 
    }              
};