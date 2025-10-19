class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, k, fill_idx = 1, 1, 1
        while i < len(nums):
            if nums[i] != nums[i-1]:
                nums[fill_idx] = nums[i]
                fill_idx += 1
                k += 1
            
            i += 1
        
        return k

