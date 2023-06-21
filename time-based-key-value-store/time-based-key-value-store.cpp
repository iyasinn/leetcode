class TimeMap {
public:
    unordered_map<string, map<int, string, greater<int>>> data;
    TimeMap() {
    }
    
    void set(string key, string value, int timestamp) {
        data[key][timestamp] = value; 
    }
    
    string get(string key, int timestamp) {

        if (!data.count(key)) return "";

        auto& m = data[key];

        auto it = m.lower_bound(timestamp);
        if (it == m.end()) return "";
        return it->second; 
        
        // while (timestamp >= 1){
        //     if (data[key].count(timestamp)){
        //         return data[key][timestamp];
        //     }
        //     timestamp--;
        // }
        // return "";
        
    }
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */