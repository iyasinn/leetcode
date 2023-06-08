// class Solution {
// public:
//     vector<vector<string>> groupAnagrams(vector<string>& strs) {
//         map<std::array<int, 26>, vector<string>> mp; 
//         for (auto&& s : strs){
//             array<int, 26> arr = {}; 
//             for (char c : s) arr[c - 'a']++;
//             mp[arr].push_back(s);
//         }
//         vector<vector<string>> sol;
//         for (auto&& [a, b] : mp){
//             sol.push_back(b);
//         }
//         return sol; 
//     }
// };


class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        using bin = array<uint8_t, 26>;
        auto m = map<bin, vector<string>>{};
        for (auto &&str : strs) {
            auto cnt = bin{};
            for (auto ch : str)     
                ++cnt[ch - 'a'];
            m[cnt].emplace_back(str);
        }
        auto res = vector<vector<string>>{};
        for (auto &&[_, group] : m)
            res.emplace_back(std::move(group));
        return res;
    }
};