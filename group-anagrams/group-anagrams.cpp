class Solution {
public:

    bool isAnagram(string s, string t){

        if (s.size() != t.size()) { return false; }
        int arr[26] = {}; 

        for (int i = 0; i < s.size(); i++){
            arr[s[i] - 'a'] += 1;
            arr[t[i] - 'a'] -= 1;
        }
        for (int i = 0; i < 26; i++){
            if (arr[i] != 0) { return false; }
        }
        return true; 
    }

    // The best approach might be a set union / unionfind approach 

    // O(numStrs * maxGroupSize * maxWordSize) -> O(n^3)
    // vector<vector<string>> groupAnagrams(vector<string>& strs) {

    //     vector<vector<string>> output;

    //     for (auto word : strs){

    //         bool notPlaced = true; 
    //         for (auto& vec : output){
    //             if (isAnagram(vec[0], word)){
    //                 notPlaced = false; 
    //                 vec.push_back(word);
    //             }
    //         }

    //         if (notPlaced){
    //             output.push_back({word});
    //         }
    //     }

    //     return output;
    // }

    vector<vector<string>> groupAnagrams(vector<string>& strs){

        unordered_map<string, vector<string>> val; 

        for (auto s : strs){
            string x = s;
            sort(x.begin(), x.end());
            val[x].push_back(s);
        }

        vector<vector<string>> output; 

        for (auto p : val){
            output.push_back(p.second);
        }

        return output;

    }
};

















