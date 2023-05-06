class Solution {
public:

    // Requires: '0' <= integer <= '9'
    inline int ctoi(char integer){
        return integer - '0';
    }

    string addBinary(string a, string b) {

        // Very important
        string output(max(a.size(), b.size()) + 1, '0');

        int oInd = output.size() - 1; 
        int aInd = a.size() - 1; 
        int bInd = b.size() - 1; 

        
        while (oInd >= 1 || aInd >= 0 || bInd >= 0){

            int sum = 0; 

            if (aInd >= 0){ sum += ctoi(a[aInd]); }
            if (bInd >= 0){ sum += ctoi(b[bInd]); }
            if (oInd >= 0){ sum += ctoi(output[oInd]); }
            
            cout << sum << " " << output << endl;

            if (sum >= 2){
                output[oInd - 1] = '1';
            }

            sum = (sum < 2) ? sum : sum - 2; 
            output[oInd] = '0' + sum;

            oInd--; 
            aInd--;
            bInd--; 
        }

        if (output[0] == '0'){
            output.erase(output.begin());
        }

        return output;
    }

};