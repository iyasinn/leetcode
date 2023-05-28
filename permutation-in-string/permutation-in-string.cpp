class Solution {
public:
    // bool checkInclusion(string s1, string s2) {

    //     if (s2.size() < s1.size()) return false;

    //     int letter[26] = {};
    //     int start = 0; 
    //     int total = 0; 

    //     for (char x : s1){
    //         letter[x - 'a']++;
    //     }

    //     for (int end = 0; end < s2.size(); end++){

    //         letter[s2[end] - 'a']--;
    //         if (end - start + 1 != s1.size()){ continue; }

    //         bool check = true; 
    //         for (auto x : letter){
    //             if (x != 0){
    //                 check = false;
    //                 break;
    //             }
    //         }

    //         if (check) return true; 

    //         cout << start << " " << endl;
            
            
    //         letter[s2[start] - 'a']++;
    //         start++; 
    //     }



    //     return false;    
    // }


    bool checkInclusion(string s1, string s2) {

        if (s2.size() < s1.size()) return false;

        int letter1[26] = {};
        int letter2[26] = {};

        // array<int, 26> letter1 = {};
        // array<int, 26> letter2 = {};
        int start = 0; 

        for (char x : s1){
            letter1[x - 'a']++;
        }

        for (int end = 0; end < s2.size(); end++){

            letter2[s2[end] - 'a']++;
            if (end - start + 1 != s1.size()){ continue; }

            if (equal(std::begin(letter1), std::end(letter1), std::begin(letter2))){
            // if (letter1 == letter2){
                return true; 
            }

            letter2[s2[start] - 'a']--;
            start++; 
        }



        return false;    
    }


};