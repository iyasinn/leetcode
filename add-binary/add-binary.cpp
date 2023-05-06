class Solution {
public:

    // Requires: '0' <= integer <= '9'
    inline int ctoi(char integer){
        return integer - '0';
    }

    string addBinary(string a, string b) {

        // Very important
        string output;
        output.reserve(max(a.size(), b.size()));
        output.push_back('0');

        int aInd = a.size() - 1; 
        int bInd = b.size() - 1; 
        
        while (aInd >= 0 || bInd >= 0){

            int sum = ctoi(output.back()); 
            if (aInd >= 0){ sum += ctoi(a[aInd]); }
            if (bInd >= 0){ sum += ctoi(b[bInd]); }

            output.back() = '0' + (sum % 2); 
            output.push_back((sum >= 2) ? '1' : '0');
            cout << output;
            aInd--;
            bInd--; 
        }

        if (output.back() == '0') { output.pop_back(); }
        
        reverse(output.begin(), output.end());

        return output;
    }

};