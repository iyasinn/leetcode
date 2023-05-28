class Solution {
public:


    int characterReplacement(string s, int k) {

        int alph[26] = {};
        unordered_map<char, int> letter;
        int best = 0; 
        int start = 0; 

        for (int end = 0; end < s.size(); end++){

            // letter[s[end]]++;
            alph[s[end] - 'A']++;

            // int maxCharCount = max_element(letter.begin(), letter.end())->second;
            int maxCharCount = alph[max_element(alph, alph + 26) - begin(alph)];

            while (start < end && (end - start + 1) - maxCharCount > k){
                alph[s[start] - 'A']--;
                // letter[s[start]]--;
                start++;
                // maxCharCount = alph[max_element(alph, alph + 26) - begin(alph)];
                // maxCharCount = max_element(letter.begin(), letter.end())->second;
            }   

            // cout << start << " " << end << endl;

            best = max(best, end - start + 1);
        }

        return best; 
        
    }
};