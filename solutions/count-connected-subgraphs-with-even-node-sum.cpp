using ll = long long; 
struct UnionFind {
    int n; 
    vector<int> par;
    vector<int> rank; 
    UnionFind(int n){
        this->n = n;
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
    void update(int x, int y){
        int px = find(x); 
        int py = find(y); 
        if (px==py){
            return; 
        }
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
        const int* ptr = &n; 
        cout << typeid(ptr).name() << endl; 
        return 0; 
    }
    // bool good(ll mask){

    // }
};