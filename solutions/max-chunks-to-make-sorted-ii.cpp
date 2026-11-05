class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        int n = arr.size();
        int furthest = 0; 
        unordered_map<int, deque<int>> idxs; 
        set<int> seen; 
        vector<pair<int, int>> vals; 


        for(int i = 0; i < n; i++){
            idxs[arr[i]].push_back(i);
            vals.push_back({arr[i], i});
            seen.insert(i);
        }
        sort(vals.begin(), vals.end(), [](auto a, auto b){return a.first<b.first;});
        unordered_map<int, deque<int>> corr; 
        for (auto p : vals){
            corr[p.first].push_back(p.second);
            cout << p.first << ": " << p.second << endl; 
        }

        int res = 0;
        for(int i = 0; i < n; i++){
            auto& q = corr[arr[i]];
            auto idx = q.front();
            q.pop_front();
            auto it = seen.lower_bound(idx);
            seen.erase(it);
            if(!seen.empty()){
                int minv = *seen.begin();
                if(minv == i+1){
                    res ++;
                }
            }
        }
        return res;
    }
};