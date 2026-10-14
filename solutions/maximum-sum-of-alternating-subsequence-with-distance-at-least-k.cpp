#include <vector>
#include <algorithm>

class SegTree {
private:
    int n;
    std::vector<long long> tree;

    void update_dfs(int node, int l, int r, int i, long long val) {
        if (l == r) {
            tree[node] = val;
            return;
        }
        int m = l + (r - l) / 2;
        if (i <= m) {
            update_dfs(2 * node, l, m, i, val);
        } else {
            update_dfs(2 * node + 1, m + 1, r, i, val);
        }
        tree[node] = std::max(tree[2 * node], tree[2 * node + 1]);
    }

    long long query_dfs(int node, int l, int r, int ql, int qr) {
        if (ql <= l && r <= qr) {
            return tree[node];
        }
        if (r < ql || l > qr) {
            return 0;
        }
        int m = l + (r - l) / 2;
        return std::max(query_dfs(2 * node, l, m, ql, qr), query_dfs(2 * node + 1, m + 1, r, ql, qr));
    }

public:
    SegTree(int n) : n(n), tree(4 * n, 0) {}

    void update(int i, long long val) {
        update_dfs(1, 0, n - 1, i, val);
    }

    long long query(int ql, int qr) {
        return query_dfs(1, 0, n - 1, ql, qr);
    }
};

class Solution {
public:
    long long maxAlternatingSum(std::vector<int>& nums, int k) {
        int n = nums.size();
        if (n == 0) return 0;
        
        int maxv = *std::max_element(nums.begin(), nums.end());
        std::vector<std::vector<long long>> dp(n, std::vector<long long>(2, 0));
        
        SegTree inc(maxv + 1);
        SegTree dec(maxv + 1);
        
        for (int i = 0; i < std::min(n, k); ++i) {
            dp[i][0] = nums[i];
            dp[i][1] = nums[i];
        }
        
        for (int i = k; i < n; ++i) {
            inc.update(nums[i - k], dp[i - k][1]);
            dec.update(nums[i - k], dp[i - k][0]);
            dp[i][0] = inc.query(nums[i] + 1, maxv) + nums[i];
            dp[i][1] = dec.query(0, nums[i] - 1) + nums[i];
        }
        
        long long max_val = 0;
        for (int i = 0; i < n; ++i) {
            max_val = std::max(max_val, dp[i][0]);
            max_val = std::max(max_val, dp[i][1]);
        }
        return max_val;
    }
};