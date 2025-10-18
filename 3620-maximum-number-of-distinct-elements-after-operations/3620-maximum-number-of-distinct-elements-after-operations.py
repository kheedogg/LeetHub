class Solution:
    def getPossibleMinimumNum(self, n: int, k: int, cmp_num: int):
        
        if cmp_num is None or cmp_num < n-k:
            return n-k
        elif cmp_num < n+k:
            return cmp_num+1
        else:
            return None

    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        sorted_lst = sorted(nums)
        ans_lst = []

        for e in sorted_lst:
            
            if ans_lst==[]:
                selection = self.getPossibleMinimumNum(e, k, None)
            else:
                selection = self.getPossibleMinimumNum(e, k, ans_lst[-1])

            if selection is not None:
                ans_lst.append(selection)    
                
        return len(ans_lst)