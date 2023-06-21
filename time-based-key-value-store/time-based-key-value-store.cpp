class TimeMap {
public:

    unordered_map<string, vector<pair<int, string>>> data;
    TimeMap() {
    }
    
    void set(string key, string value, int timestamp) {
        data[key].push_back({timestamp, value}); 
    }
    
    string get(string key, int timestamp) {

        if (!data.count(key)) return "";
        auto& vec = data[key];


        // auto it = upper_bound(begin(data[key]), end(data[key]), pair<int, string>(timestamp, ""), [](
        // const pair<int, string>& a, const pair<int, string>& b) { return a.first < b.first; });
        // return it == data[key].begin() ? "" : prev(it)->second;

        auto it = upper_bound(vec.begin(), vec.end(), pair<int, string>({timestamp, ""}), 
                              [](const pair<int, string> a, const pair<int, string> b)
                                {
                                    return a.first < b.first;
                                });

        return (it == data[key].begin()) ? "" : prev(it)->second;
        // return (it != vec.end()) ? it->second : ""; 
            
    }
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */