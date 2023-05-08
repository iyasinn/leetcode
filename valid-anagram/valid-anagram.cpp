class Solution {
public:

    // Simple array indexing method 
    // O(n^2) time, O(1) space
    // Uses a swap method to consider if we've seen something or not ijuhk
    // bool isAnagram(string s, string t) {

    //     if (s.size() != t.size()) return false;
    //     int n = s.size(); 

    //     for (int i = 0; i < n; i++){

    //         // This loops searches for s[i] in some t[j], and swaps t[i] with that t[j]
    //         for (int j = i; j < n; j++){
    //             if (s[i] == t[j]){
    //                 swap(t[i], t[j]);
    //                 break;
    //             }
    //         }

    //         if (s[i] != t[i]) return false; 
    //     }

    //     return true; 
    // }
    
    // O(n) 
    // bool isAnagram(string s, string t){

    //     if (s.size() != t.size()){ return false; }
    //     const int SIZE = s.size();

    //     unordered_map<char, int> val;

    //     for (int i = 0; i < SIZE; i++){
    //         val[s[i]]++;
    //         val[t[i]]--;
    //     }

    //     for (auto v : val){
    //         if (v.second != 0){ return false; }
    //     }

    //     return true; 
    // }

    bool isAnagram(string s, string t){
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        return s == t; 
    }




};