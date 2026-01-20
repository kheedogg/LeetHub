class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            found = -1
            # brute force search
            for i in range(n):
                if i | (i+1) == n:
                    found = i
                    break
            ans.append(found)
        return ans