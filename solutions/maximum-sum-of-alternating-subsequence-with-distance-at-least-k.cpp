class Solution {
    struct SegTree {
        int n;
        vector<int> tree;

        SegTree(int n) : n(n), tree(4 * n, 0) {}

        void update(int i, int val, int node, int l, int r) {
            if (l == r) {
                tree[node] = max(tree[node], val);
                return;
            }

            int m = (l + r) / 2;
            if (i <= m)
                update(i, val, 2 * node, l, m);
            else
                update(i, val, 2 * node + 1, m + 1, r);

            tree[node] = max(tree[2 * node], tree[2 * node + 1]);
        }

        void update(int i, int val) {
            update(i, val, 1, 0, n - 1);
        }

        int query(int ql, int qr, int node, int l, int r) {
            if (r < ql || l > qr) return 0;
            if (ql <= l && r <= qr) return tree[node];

            int m = (l + r) / 2;
            return max(
                query(ql, qr, 2 * node, l, m),
                query(ql, qr, 2 * node + 1, m + 1, r)
            );
        }

        int query(int ql, int qr) {
            if (ql > qr) return 0;
            return query(ql, qr, 1, 0, n - 1);
        }
    };

public:
    long long maxAlternatingSum(vector<int>& nums, int k) {
        int n = nums.size();
        int maxv = *max_element(nums.begin(), nums.end());

        vector<array<long long, 2>> dp(n);
        SegTree inc(maxv + 1), dec(maxv + 1);

        long long ans = 0;

        for (int i = 0; i < min(k, n); i++) {
            dp[i] = {nums[i], nums[i]};
            ans = max(ans, (long long)nums[i]);
        }

        for (int i = k; i < n; i++) {
            int x = nums[i - k];

            inc.update(x, dp[i - k][0]);
            dec.update(x, dp[i - k][1]);

            dp[i][0] = nums[i] + inc.query(nums[i] + 1, maxv);
            dp[i][1] = nums[i] + dec.query(0, nums[i] - 1);

            ans = max({ans, dp[i][0], dp[i][1]});
        }

        return ans;
    }
};