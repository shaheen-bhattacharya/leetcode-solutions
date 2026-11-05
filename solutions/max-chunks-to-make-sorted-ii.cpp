class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        int n = arr.size();
        int furthest = 0; 
        set<int> seen; 
        vector<pair<int, int>> vals; 
        vector<int> narr = arr; 
        sort(narr.begin(), narr.end());
        unordered_map<int, deque<int>> corr; 


        for(int i = 0; i < n; i++){
            corr[arr[i]].push_back(i);
            seen.insert(i);

        }
        for (auto p : vals){
            corr[p.first].push_back(p.second);
        }

        int res = 0;
        for(int i = 0; i < n; i++){
            auto& q = corr[arr[i]];
            auto idx = q.front();
            q.pop_front();
            auto it = seen.lower_bound(idx);
            cout << arr[i] << ", idx: " << idx << endl; 
            seen.erase(it);
            if(!seen.empty()){
                int minv = *seen.begin();
                if(minv == i+1){
                    res++;
                }
            }
        }
        return res;
    }
};