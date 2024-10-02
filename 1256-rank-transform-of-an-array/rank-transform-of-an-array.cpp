/*
What tips you to a certain solution? 
And for arrays, theres many approaches

Ranks go from smaller to larger 
There is a sorting constraint on the solution


-------

it would be nice 
hashmap[number] = rank
because we need to operate on our original array 

*/


class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {


        auto _set = (std::set<int>(arr.begin(), arr.end())); 
        auto vec = vector<int>(_set.begin(), _set.end()); 
        std::unordered_map<int, int> m; 

        for (int i = 0; i < vec.size(); i++){
            m[vec[i]] = i + 1; 
        }

        for (int i = 0; i < arr.size(); i++){
            arr[i] = m[arr[i]]; 
        }

        return arr; 

        // The rank is (index + 1)
        // given an element in arr, we could look for it inside vec
        // finding the element O(N). --> Overall O(N^2)
        // finding the element O(log(n)) --> O(N log N)

        // Hashmap which maps numbers to numbers 
        // number -> rank 
        // thsi O(1) --> O(N) solution

        // [1, 3, 5, 10]


        return {}; 

    }
};

