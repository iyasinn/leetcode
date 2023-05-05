class Solution {
public:

    bool isVowel(char c){
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }

    int maxVowels(string s, int k) {

        if (s.size() < k) { return 0; } 

        int start = 0; 
        int best = 0; 
        int curr = 0; 

        for (int i = 0; i < k; i++){
            if (isVowel(s[i])){ curr++; }
        }

        best = curr; 

        for (int end = k; end < s.size(); end++){
            if (isVowel(s[end])){ curr++; }
            if (isVowel(s[start])){ curr--; }
            best = max(curr, best);
            start++; 
        }


        return best; 
    }
};