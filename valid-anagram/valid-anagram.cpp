class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        int n = s.size(); 

        for (int i = 0; i < n; i++){

            // This loops searches for s[i] in some t[j], and swaps t[i] with that t[j]
            for (int j = i; j < n; j++){
                if (s[i] == t[j]){
                    swap(t[i], t[j]);
                    break;
                }
            }

            if (s[i] != t[i]) return false; 
        }

        return true; 
    }
};