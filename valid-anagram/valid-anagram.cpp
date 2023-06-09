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
    
    // O(n) time, O(1) space BECAUSE there are ONLY 26 alphabet characters
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

    // O(n log n) time copmlexity, O(1) space
    // bool isAnagram(string s, string t){
    //     if (s.size() != t.size()) return false; 
    //     sort(s.begin(), s.end());
    //     sort(t.begin(), t.end());
    //     return s == t; 
    // }

    // O(n) solution, O(1) space
    // This soltuion made me ralize the importance of sometime suisn simple DS
    // Sometimes if you have constant things to cmopare, maybe just make a constan tarray
    // So any constant should be turned into a thing we can use
    // SPECIFICLALY, A CONSTANT ORDERED set of data can be turned into an O(1) space HASHAMP
    // This is just a direct mapped array here tbh 
    bool isAnagram(string s, string t){

        if (s.size() != t.size()) { return false; }

        // Zero initialized?
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


};