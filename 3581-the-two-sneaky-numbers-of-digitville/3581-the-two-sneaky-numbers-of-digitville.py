class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        from collections import Counter
        freq = Counter(nums)

        ans = []
        for k, v in freq.items():
            if v == 2:
                ans.append(k)
                if len(ans) == 2:
                    return ans
        
        return ans