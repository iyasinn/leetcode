class Solution {
public:
    bool checkInclusion(string s1, string s2) {

        // Max size is 26
        vector<int> arr1(26, 0); 
        for (char c : s1){ arr1[c - 'a']++; }

        vector<int> arr2(26, 0);

        int start = 0;

        for (int end = 0; end < s2.size(); end++){

            arr2[s2[end] - 'a']++; 

            if (end - start + 1 < s1.size()){
                continue; 
            }

            if (arr1 == arr2) return true; 

            arr2[s2[start] - 'a']--; 
            start++; 
        }

        return false; 
        
    }
};