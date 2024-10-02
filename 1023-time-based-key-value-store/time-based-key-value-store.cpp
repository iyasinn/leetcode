class TimeMap {
public:

    std::unordered_map<std::string, std::vector<std::pair<int, std::string>>> m;

    TimeMap() {
    }
    
    void set(string key, string value, int timestamp) {
        m[key].push_back(std::make_pair(timestamp, value)); 
    }
    
    string get(string key, int timestamp) {

        const auto& vec = m[key]; 
        int l = 0, r = vec.size();
        int solution = -1; 

        while (l < r){
            int mid = l + ((r - l) / 2);

            if (vec[mid].first <= timestamp){
                l = mid + 1; 
                solution = mid; 
            }
            else {
                r = mid; 
            }
        }

        return solution == -1 ? "" : vec[solution].second; 

    }
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */