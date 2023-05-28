class Solution {
public:


    int characterReplacement(string s, int k) {

        int alph[26] = {};
        int best = 0; 
        int start = 0; 

        for (int end = 0; end < s.size(); end++){
            alph[s[end] - 'A']++;
            int maxCharCount = alph[max_element(alph, alph + 26) - begin(alph)];

            while (start < end && (end - start + 1) - maxCharCount > k){
                alph[s[start] - 'A']--;
                start++;
            }   
            best = max(best, end - start + 1);
        }

        return best; 
        
    }
};