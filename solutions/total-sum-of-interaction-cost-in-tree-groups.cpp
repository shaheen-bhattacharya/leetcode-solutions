class Solution {
public:
    vector<int> total;
    int res;
    long long interactionCosts(int n, vector<vector<int>>& edges, vector<int>& group) {
        unordered_map<int, vector<int>> adj; 
        for (auto& e : edges){
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }
        total.resize(21);
        for(int i = 0; i < n; i++){
            total[group[i]]++;
        }
        res = 0; 
        dfs(-1, 0, adj, group);
        return res;

    }
    vector<int> dfs(int par, int node, auto& adj, auto& group){
        vector<int> freq(21, 0);
        for (auto nei : adj[node]){
            if (nei == par) continue; 
            vector<int> chf = dfs(node, nei, adj, group);
            for(int g = 0; g <= 20; g++){
                freq[g] += chf[g];
                res += (total[g] - chf[g]) * chf[g];
            }
        }
        freq[group[node]]++;
        return freq;
    }
};