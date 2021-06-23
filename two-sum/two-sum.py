class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a= []
        for i, val1 in enumerate(nums):
            val2 = target - val1
            if val2 in nums[i+1:]:
                a.append(i)
                a.append(nums[i+1:].index(val2) + i + 1)
        return a