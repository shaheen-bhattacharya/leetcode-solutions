#include <vector>
#include <unordered_map>

class Solution {
public:
    int countStaircase(std::vector<int>& nums) {
        int n = nums.size();
        int res = 0;
        
        // Precompute triangular numbers and their corresponding k
        std::unordered_map<int, int> tri;
        long long ln = 0;
        int k = 0;
        while (ln <= n) {
            k++;
            ln += k;
            tri[ln] = k;
        }
        
        for (int i = 0; i < n; ++i) {
            std::unordered_map<int, int> freq;
            std::unordered_map<int, int> pos_map;
            int seen_len = 0;
            
            for (int j = i; j < n; ++j) {
                int val = nums[j];
                if (freq.find(val) == freq.end()) {
                    freq[val] = 0;
                    seen_len++;
                    pos_map[val] = seen_len;
                }
                freq[val]++;
                
                // Pruning: If any value's frequency exceeds its required position, 
                // it can never satisfy the staircase condition.
                if (freq[val] > pos_map[val]) {
                    break;
                }
                
                int length = j - i + 1;
                // Check if the length matches a valid staircase length for current distinct count
                auto it = tri.find(length);
                if (it != tri.end() && it->second == seen_len) {
                    res++;
                }
            }
        }
        
        return res;
    }
};