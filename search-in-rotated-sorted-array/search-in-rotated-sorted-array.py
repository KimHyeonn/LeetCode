class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)-1
        if target not in nums:
            return -1
        
        else:
            while (nums[i] != target) & (nums[j] != target):
                i += 1
                j -= 1
            
            if nums[i] == target:
                return i
            else:
                return j
                