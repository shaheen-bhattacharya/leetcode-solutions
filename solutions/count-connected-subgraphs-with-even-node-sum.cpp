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
        rank.resize(n, 0); 
    }
    int find(int x){
        while(x != par[x]){
            par[par[x]] = par[x];
            par[x] = x; 
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
        if (px < py){
            par[px] = py; 
        }else if (px > py){
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
        for(ll mask = 0; mask < pow(2, n)-1; mask++){
            res += good(mask, n, adj);
        }
        return res; 
    }
    bool good(ll mask, int& n, auto& adj){
        UnionFind uf(n);
        int ones = __builtin_popcount(mask);
        for(int i = 0; i < n; i++){
            if (mask & (1 << i)){
                for (auto nei : adj[i]){
                    if (mask & (1 << i)){
                        uf.unite(i, nei);
                    }
                }
            }
        }
        return uf.comps == n - ones + 1; 
    }
};