class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0:
            return 0
        else:
            x = 1
            for i in range(1, l):
                if nums[i] == nums[i-1]:
                    pass
                elif nums[i] > nums[i-1]:
                    nums[x] = nums[i]
                    x+=1
                    
            return x