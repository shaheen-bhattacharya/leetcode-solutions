class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mindx = 0
        maxdx = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i] > nums[maxdx]:
                maxdx = i
            if nums[i] < nums[mindx]:
                mindx = i
        i, j = min(mindx, maxdx), max(mindx, maxdx)
        return min(i + n - j, j+1, n-i-1)
        print(i+n-j-1)
    
            