struct Query{
    int l, r, idx, k; 
};
struct BIT{
    int n;
    vector<int> bit; 
    BIT(int n){
        this->n = n; 
        bit.resize(n+1, 0);
    }   
    void update(int i, int val){
        while (i <= n){
            bit[i] += val; 
            i += i & -i; 
        }
    }
    int query(int i){
        int res = 0; 
        while (i > 0){
            res += bit[i];
            i -= i & -i; 
        }
        return res; 
    }
    int kth(int k){
        int idx = 0; 
        int pw = 1;
        while(pw*2 <= n){
            pw*=2;
        }
        for (; pw > 0; pw/=2){
            int next = idx + pw; 
            if(next <= n && bit[next] < k){
                idx = next; 
                k -= bit[next];
            }
        }
        return idx+1;
    }
};
class Solution {
public:
    vector<int> pref; 
    int timer = 0; 
    vector<int> tin; 
    vector<int> tout;
    vector<int> tree;  
    unordered_map<int, int> freq; 
    const int MAXX = 1 << 17; 
    BIT bit{MAXX}; 

    vector<int> kthSmallest(vector<int>& par, vector<int>& vals, vector<vector<int>>& queries) {
        int n = par.size();
        int blocks = int(sqrt(n)); 
        int nq = queries.size();
        bit.n = MAXX;
        unordered_map<int, vector<int>> adj; 
        pref.resize(n);
        tin.resize(n);
        tout.resize(n);
        pref[0] = vals[0];
        for(int i = 0; i < n; i++){
            adj[par[i]].push_back(i);
        }
        tour(0, adj);
        dfs(0, vals, adj); 
        vector<Query> q2; 
        for(int i = 0; i < nq; i++){
            auto& q = queries[i];
            Query qo(tin[q[0]], tout[q[0]]-1, i, q[1]);
            q2.push_back(qo);
        }
        sort(q2.begin(), q2.end(), [&](const Query& a, const Query& b){
            int ba = a.l / blocks;
            int bb = b.l / blocks;
            if (ba != bb){
                return ba < bb; 
            }
            return a.r < b.r; 
        });

        int cl = 0, cr = -1; 
        vector<int> res(nq); 
        for (auto& q : q2){
            while (cl > q.l) add(--cl);
            while (cr < q.r) add(++cr);
            while (cl < q.l) remove(cl++);
            while (cr > q.r) remove(cr--);
            int qv = bit.query(MAXX);
            if (qv < q.k){
                res[q.idx] = -1; 
            }else{
                res[q.idx] = bit.kth(q.k)-1;
            }
        }
        return res;
    }
    void dfs(int node, auto& vals, auto& adj){
        for (int nei : adj[node]){
            pref[nei] = pref[node] ^ vals[nei];
            dfs(nei, vals, adj);
        }
    }
    void tour(int node, auto& adj){
        tin[node] = timer++; 
        tree.push_back(node); 
        for (auto nei : adj[node]){
            tour(nei, adj); 
        }
        tout[node] = timer; 
    }
    void add(int i){
        int val = pref[tree[i]]+1;
        if (freq[val] == 0){
            bit.update(val, 1);
        }
        freq[val]++;
    }
    void remove(int i){
        int val = pref[tree[i]]+1;
        if (freq[val] == 1){
            bit.update(val, -1);
        }
        freq[val]--;
    }   
};