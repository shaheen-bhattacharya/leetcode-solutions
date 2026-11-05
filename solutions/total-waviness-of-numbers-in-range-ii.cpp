using ll = long long;
class Solution {
public:
    pair<ll, ll> dp[16][11][11][2][2];
    long long totalWaviness(long long num1, long long num2) {
        return good(num2) - good(num1-1);
    }
    ll good(ll num){
        memset(dp, -1, sizeof(dp));
        string snum = to_string(num);
        int sn = snum.size();
        return dfs(snum, sn, 0, 10, 10, 1, 0).first;
    }
    pair<ll, ll> dfs(string& snum, int sn, int i, int prev, int curr, int tight, int started){
        if(i==sn){
            return {0, started};
        }
        if(!dp[i][prev][curr][tight][started].first != -1){
            return dp[i][prev][curr][tight][started];
        }
        int cd = snum[i] - '0';
        int ub = tight ? cd : 9;
        ll totw = 0;
        ll totc = 0;
        for(int d = 0; d <= ub; d++){
            int ntight = tight && cd == d; 
            int nst = started || d != 0;
            if (!nst){
                auto [w, c] = dfs(snum, sn, i+1, prev, curr, ntight, nst);
                totw += w;
                totc += c;
            }else if(!started){
                auto[w, c] = dfs(snum, sn, i+1, curr, d, ntight, nst);
                totw += w; 
                totc += c; 
            }else{
                auto[w, c] = dfs(snum, sn, i+1, curr, d, ntight, nst);
                totc += c;
                totw += w;
                if(prev != 10 && ((curr > prev && curr > d) || (curr < prev && curr < d))){
                    totw += c;
                }
            }
        }
        dp[i][prev][curr][tight][started] = {totw, totc};
        return dp[i][prev][curr][tight][started];
    }
};