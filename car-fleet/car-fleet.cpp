class Solution {
public:

    
    // O (n log n) time and O(1) space
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
            if (currTime > time){
                count++;
                time = currTime; 
            }
        }
    
        return count; 
    }
    
    










};




// struct Car {
//     int position;
//     int speed;

//     Car(int p, int s) {
//         position = p;
//         speed = s;
//     }
// };

// struct PositionComparator {
//     bool operator()(const Car& c1, const Car& c2) const {
//         return c1.position < c2.position;
//     }
// };

// class Solution {
// public:
//     // Returns true iff cars i and j would bump into each other
//     // before reaching target, in a world with no other cars.
//     bool bump(vector<Car>& cars, int target, int i, int j) {
//         return cars[i].speed * (long)cars[j].position - cars[j].speed * (long)cars[i].position <= target * (long)(cars[i].speed - cars[j].speed);
//     }

//     int carFleet(int target, vector<int>& position, vector<int>& speed) {
//         vector<Car> cars;
//         int n = position.size();
//         for (int i = 0; i < n; ++i) {
//             cars.push_back(Car(position[i], speed[i]));
//         }
//         sort(cars.begin(), cars.end(), PositionComparator());
        
//         int fleets = 1;
//         int current_lead = n - 1;
//         for (int i = n - 2; i >= 0; --i) {
//             if (not bump(cars, target, i, current_lead)) {
//                 ++fleets;
//                 current_lead = i;
//             }
//         }

//         return fleets;
//     }
// };










































