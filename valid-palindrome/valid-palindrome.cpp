class Solution {
public:

    // Stack technique
    // O(n) time, O(n) space
    // bool isPalindrome(string s) {
    //     stack<char> word; 

    //     for (char c : s){
    //         if (isalnum(c)) word.push(tolower(c));
    //     }

    //     for (char c : s){
    //         if (isalnum(c)){
    //             if (word.top() != tolower(c)) return false; 
    //             word.pop();
    //         }
    //     }

    //     return true; 
    // }

    // Will try two pointer
    // bool isPalindrome(string s) {


    //     char* start = &s[0]; 
    //     char* end = &s.back();

    //     // Pointers in chars are consecutve
    //     while (start < end){
    //         // Need the start < end check, since it fails, then start = end
    //         // Which means we are in the middle, which means we have a valid palindrome
    //         while (!isalnum(*start) && start < end) start++; 
    //         while (!isalnum(*end) && start < end) end--; 

    //         if (tolower(*start) != tolower(*end)) return false; 

    //         start++; 
    //         end--; 
    //     }

    //     return true; 
    // }

    bool isPalindrome(string s){
        int start = 0; 
        int end = s.size() - 1; 

        while (start < end){
            if (!isalnum(s[start])){
                start++;
            }
            else if (!isalnum(s[end])){
                end--; 
            }
            else{
                if (tolower(s[start++]) != tolower(s[end--])) return false; 
            }
        }
        return true; 
    }



};