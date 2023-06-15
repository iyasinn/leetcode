class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int count = 1; 
        vector<pair<int, int>> v(position.size()); 
        for (int i = 0; i < v.size(); i++){
            v[i].first = position[i];
            v[i].second = speed[i];
        }

        sort(v.begin(), v.end());


        double time = (target - v[v.size() - 1].first) / static_cast<double>(v[v.size() - 1].second);
        for (int i = v.size() - 1; i >= 0; i--){

            
            double currTime = (target - v[i].first) / static_cast<double>(v[i].second);  
            cout << v[i].first << " " << time << " " << currTime << endl;

            if (currTime > time){
                count++;
                time = currTime; 
            }
        }

        return count; 

    }
};