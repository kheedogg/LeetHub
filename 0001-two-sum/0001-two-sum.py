class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, e in enumerate(nums):
            num = target - e
            if num in seen:
                return [seen[num], i]
            else:
                seen[e] = i