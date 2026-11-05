/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    int numComponents(ListNode* head, vector<int>& nums) {
        int n = nums.size(); 
        unordered_set<int> st; 
        for(int i = 0; i < n; i++){
            st.insert(nums[i]);
        }
        ListNode* tmp = head; 
        int res = 0;
        while (tmp){  
            if (!st.count(tmp->val)){
                tmp = tmp->next; 
                continue; 
            }
            while(tmp && st.count(tmp->val)){
                tmp = tmp->next; 
            }
            res += 1; 
        }
        return res; 
    }
};