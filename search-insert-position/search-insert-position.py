class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        if nums[i] >= target:
            return i
        
        elif nums[-1] < target:
            return len(nums)
        
        else:
            while nums[i] < target:
                i += 1
                
                if nums[i] >= target:
                    
                    return i