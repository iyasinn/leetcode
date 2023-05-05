class Solution {
public:

    bool isVowel(char c){
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }

    int maxVowels(string s, int k) {

        int start = 0; 
        int best = 0; 
        int curr = 0; 

        for (int end = 0; end < s.size(); end++){
            if (isVowel(s[end])){ curr++; }

            if (end - start == k){
                curr -= (isVowel(s[start]));
                start++;
            }

            best = max(curr, best); 
        }


        return best; 
    }
};