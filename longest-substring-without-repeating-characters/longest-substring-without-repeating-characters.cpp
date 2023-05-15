class Solution {
public:
    int lengthOfLongestSubstring(string s) {

        unordered_map<char, int> letters;
        int start = 0; 
        int best = 0; 

        for (int end = 0; end < s.size(); end++){
            
            letters[s[end]]++;

            while(start < end && letters[s[end]] > 1){
                letters[s[start]]--;
                start++; 
            }

            best = max(best, end - start + 1);
        }

        return best; 
    }
};