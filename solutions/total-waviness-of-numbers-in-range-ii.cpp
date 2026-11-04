using ll = long long;
class Solution {
public:
    ll dp[16][11][11][2][2];
    long long totalWaviness(long long num1, long long num2) {
        memset(dp, -1, sizeof(dp));
        return good(num2) - good(num1-1);
    }
    int good(ll num){
        string snum = to_string(num);
        int sn = snum.size();
        return dfs(snum, sn, 0, 10, 10, 1, 0);
    }
    ll dfs(string& snum, int sn, int i, int prev, int curr, int tight, int started){
        if(dp[i][prev][curr][tight][started] != -1){
            return dp[i][prev][curr][tight][started];
        }
        if(i==sn){return 0;}
        int cd = snum[i] - '0';
        int ub = tight ? cd : 9;
        ll res = 0; 
        for(int d = 0; d <= ub; d++){
            int ntight = tight && cd == d; 
            int nst = started || d != 0;
            if (!nst){
                res += dfs(snum, sn, i+1, prev, curr, ntight, nst);
                continue; 
            }
            if(prev != 10 && ((curr > prev && curr > d) || (curr < prev && curr < d))){
                res += 1 + dfs(snum, sn, i+1, curr, d, ntight, nst);
            }else{
                res += dfs(snum, sn, i+1, curr, d, ntight, nst);
            }
        }
        dp[i][prev][curr][tight][started] = res;
        return res;
    }
};