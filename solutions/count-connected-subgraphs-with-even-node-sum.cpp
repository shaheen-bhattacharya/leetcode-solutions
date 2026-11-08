using ll = long long; 
struct UnionFind {
    int n; 
    int comps; 
    vector<int> par;
    vector<int> rank; 
    UnionFind(int n){
        this->n = n;
        comps = n; 
        par.resize(n);
        iota(par.begin(), par.end(), 0);
        rank.resize(n, 0); 
    }
    int find(int x){
        while(x != par[x]){
            par[par[x]] = par[x];
            x = par[x];  
        }
        return x; 
    }
    void unite(int x, int y){
        int px = find(x); 
        int py = find(y); 
        if (px==py){
            return; 
        }
        comps--; 
        if (rank[px] < rank[py]){
            par[px] = py; 
        }else if (rank[px] > rank[py]){
            par[py] = px; 
        }else{
            par[px] = py; 
            rank[py]++;
        }
    }
};
class Solution {
public:
    int evenSumSubgraphs(vector<int>& nums, vector<vector<int>>& edges) {
        unordered_map<int, vector<int>> adj; 
        for (auto edge : edges){
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }
        int n = nums.size(); 
        int res = 0;
        for(ll mask = 1LL; mask < (1LL << n); mask++){
            res += good(mask, n, adj, nums);
        }
        return res; 
    }
    bool good(ll mask, int& n, auto& adj, auto& nums){
        UnionFind uf(n);
        int ones = __builtin_popcountll(mask);
        int tot = 0;
        for(int i = 0; i < n; i++){
            if (mask & (1LL << i)){
                tot += nums[i];
                for (auto nei : adj[i]){
                    if (mask & (1LL << nei)){
                        uf.unite(i, nei);
                    }
                }
            }
        }
        // cout << uf.comps << " " << n - ones; 
        return tot%2 == 0 && uf.comps == n - ones + 1; 
    }
};