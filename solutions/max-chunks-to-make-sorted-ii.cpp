class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        int n = arr.size();
        int furthest = 0; 
        unordered_map<int, deque<int>> idxs; 

        for(int i = 0; i < n; i++){
            idxs[arr[i]].push_back(i);
        }
        int res = 0;
        for(int i = 0; i < n; i++){
            deque<int>& q = idxs[arr[i]];
            int fidx = q.front();
            q.pop_front(); 
            furthest = max(furthest, fidx); 
            if (furthest==i){
                res += 1;
            }
        }
        return res;
    }
};