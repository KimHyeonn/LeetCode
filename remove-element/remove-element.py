class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        l = len(nums)
        while val in nums:
            nums.pop(nums.index(val))
            i += 1
        
        k = l - i
        return k