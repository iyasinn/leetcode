class Solution {
public:

    // we can view the movement of this number as a graph

    int calcSum(int n){
        int sum = 0;
        while (n){
            sum += (n % 10) * (n % 10);
            n = n / 10;
        }
        return sum;
    }


    bool isHappy(int n) {
        int start = n;
        int end = calcSum(calcSum(n));

        while (start != end){
            start = calcSum(start);
            end = calcSum(calcSum(end));
            
            if (end == 1) return true;
        }

        return end == 1; 
    }
};