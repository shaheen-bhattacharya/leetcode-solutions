using ll = long long; 
class Solution {
public:
    ll inf = 1e18; 
    int minActivationCost(vector<vector<int>>& edges, vector<int>& values) {
        ll res = inf; 
        int n = values.size(); 
        vector<ll> best(n, inf);
        for (auto& e : edges){
            int u = e[0], v = e[1];
            ll w = e[2];
            int pu = __builtin_popcount(values[u])%2; 
            int pv = __builtin_popcount(values[v])%2;
            if (pu == pv){
                res = min(res, w);
            }else{
                int zn = (pu == 0) ? u : v;
                res = min(res, best[zn]+w);
                best[zn] = min(best[zn], w);
            }
        }
        return (res >= inf) ? -1 : res; 
    }
};