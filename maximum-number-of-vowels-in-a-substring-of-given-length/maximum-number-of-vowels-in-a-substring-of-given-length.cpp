class Solution {
public:

    bool isVowel(char c){
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }

    int maxVowels(string s, int k) {

        if (s.size() < k) { return 0; } 

        int start = 0; 
        int end = k - 1; 
        int best = 0; 
        int curr = 0; 

        for (int i = 0; i < k; i++){
            if (isVowel(s[i])){ curr++; }
        }

        best = curr; 

        while (end < s.size()){

            if (end == s.size() - 1){
                return best; 
            }     

            if (isVowel(s[end + 1])){ curr++; }
            if (isVowel(s[start])){ curr--; }

            best = max(curr, best);

            start++; 
            end++; 
        }


        return best; 
    }
};