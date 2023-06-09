class Solution {
public:

    // // O(n * k) 
    // vector<int> maxSlidingWindow(vector<int>& n, int k) {

    //     vector<int> res; 
    //     int start = 0; 

    //     for (int end = 0; end < n.size(); end++){

    //         // Did end++ by accident, when in a for loop this doesn't matter since it will increment anyway
    //         if (end - start + 1 < k){
    //             // end++
    //             continue; 
    //         }

    //         if (end - start + 1 > k){
    //             start++; 
    //         }

    //         res.push_back(*max_element(n.begin() + start, n.begin() + end + 1));
    //     }

    //     return res;    
    // }

    // ----------------------------------------------

    // struct Element {
    //     int val; 
    //     int index; 
    // };
    
    // // O(n * log(n))
    // vector<int> maxSlidingWindow(vector<int>& n, int k) {

    //     vector<int> res; 
    //     int start = 0; 
    //     auto comp = [](Element a, Element b){ return a.val <= b.val; };
    //     priority_queue<Element, vector<Element>, decltype(comp)> pq(comp);


    //     for (int end = 0; end < n.size(); end++){

    //         pq.push({n[end], end});

    //         if (end - start + 1 < k){
    //             continue; 
    //         }

    //         while (pq.top().index < start){
    //             pq.pop(); 
    //         }

    //         res.push_back(pq.top().val);
    //         start++; 
    //     }

    //     return res;    
    // }


    // ----------------------------------------------
    
    // O(n * log(n))
    vector<int> maxSlidingWindow(vector<int>& n, int k) {

        vector<int> res; 
        int start = 0; 
        multiset<int> ms; 

        for (int end = 0; end < n.size(); end++){
            
            ms.insert(n[end]);

            if (end - start + 1 < k){ continue; } 
            res.push_back(*ms.rbegin());

            ms.erase(ms.find(n[start]));
            start++;  
        }

        return res;    
    }
};



