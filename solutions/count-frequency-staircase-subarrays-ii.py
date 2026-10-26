class Solution:
    def countStaircase(self, nums: list[int]) -> int:        
        n = len(nums)
        res = n
        lgt = 3
        curr = 3
        sqv = {}
        ln = 1
        cv = 2
        while ln <= n:
            sqv[ln] = [cv-1,cv]
            ln += cv
            cv += 1
        
        while lgt <= n:
            dlen = sqv[lgt][0]
            idxs = defaultdict(deque)
            seen = SortedList()
            
            for i in range(lgt):
                idxs[nums[i]].append(i)
                if len(idxs[nums[i]]) == 1:
                    seen.add((i, nums[i]))
            if len(seen) == dlen:
                p = 1
                flag = True
                for _, v in seen:
                    if len(idxs[v]) != p:
                        flag = False
                        break
                    p += 1
                if flag:
                    res += 1
                    
            for i in range(lgt, n):
                b = idxs[nums[i-lgt]].popleft()
                seen.remove((b,nums[i-lgt]))
                
                if len(idxs[nums[i-lgt]]) > 0:
                    seen.add((idxs[nums[i-lgt]][0], nums[i-lgt]))
                    
                idxs[nums[i]].append(i)
                if len(idxs[nums[i]]) == 1:
                    seen.add((i, nums[i]))
                    
                if len(seen) == dlen:
                    p = 1
                    flag = True
                    for _, v in seen:
                        if len(idxs[v]) != p:
                            flag = False
                            break
                        p += 1
                    if flag:
                        res += 1
            lgt += curr
            curr += 1
        return res

                
            
        
        
        
        
