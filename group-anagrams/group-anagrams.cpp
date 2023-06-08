class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<std::array<int, 26>, vector<string>> mp; 
        for (auto&& s : strs){
            array<int, 26> arr = {}; 
            for (char c : s) arr[c - 'a']++;
            mp[arr].push_back(s);
        }
        vector<vector<string>> sol;
        for (auto&& vec : mp){
            sol.push_back(vec.second);
        }
        return sol; 
    }
};