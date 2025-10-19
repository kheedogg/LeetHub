class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, fill_idx = 1, 1
        status = [nums[0], None]
        while i < len(nums):
            if status[0] == nums[i]:
                if status[1] != nums[i]:
                    status[1] = nums[i]
                    nums[fill_idx] = nums[i]
                    fill_idx += 1
            else:
                status = [nums[i], None]
                nums[fill_idx] = nums[i]
                fill_idx += 1
            
            i += 1
            
        
        return fill_idx