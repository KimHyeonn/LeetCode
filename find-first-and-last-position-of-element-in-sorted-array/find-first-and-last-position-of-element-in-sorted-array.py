class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a = []
        if target not in nums:
            return [-1,-1]
        
        if len(nums) == 1:
            return [0, 0]
        
        else:
            for i in range(0,len(nums)):
                if nums[i] == target:
                    a.append(i)
                    
            return [a[0], a[-1]]