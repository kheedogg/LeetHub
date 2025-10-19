class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, k, fix_idx = 0, 0, 0
        while i < len(nums):
            if nums[i] != val:
                nums[fix_idx] = nums[i]
                fix_idx += 1
                k += 1
            
            i += 1
        
        return k
            


