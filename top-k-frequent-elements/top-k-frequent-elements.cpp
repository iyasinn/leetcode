class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {

        unordered_map<int, int> count;
        for (auto val : nums){
            count[val]++;
        }

        auto cmp = [](pair<int, int> a, pair<int, int> b){ return a.second >= b.second; };

        priority_queue<pair<int, int>, 
                       vector<pair<int, int>>, 
                       decltype(cmp)> 
                       pq(cmp); 
        

        for (pair<const int, int>& x : count){
            pq.push(x);
            if (pq.size() > k){ pq.pop(); }
        }

        vector<int> sol; 
        sol.reserve(k);

        while (!pq.empty()){
            sol.emplace_back(move(pq.top().first));
            pq.pop();
        }

        return sol;
    }
};