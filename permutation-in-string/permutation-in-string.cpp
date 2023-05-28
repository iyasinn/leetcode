class Solution {
public:
    bool checkInclusion(string s1, string s2) {

        if (s2.size() < s1.size()) return false;

        int letter[26] = {};
        int start = 0; 

        for (char x : s1){
            letter[x - 'a']++;
        }

        for (int end = 0; end < s2.size(); end++){

            letter[s2[end] - 'a']--;
            if (end - start + 1 != s1.size()){ continue; }

            bool check = true; 
            for (auto x : letter){
                if (x != 0){
                    check = false;
                    break;
                }
            }

            if (check) return true; 

            cout << start << " " << endl;
            
            
            letter[s2[start] - 'a']++;
            start++; 
        }



        return false; 

        
    }
};