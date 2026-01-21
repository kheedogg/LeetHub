class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            bin_lst = list(bin(n))[2:]
            if bin_lst[-1] == "0": # 짝수는 ans가 존재할 수 없음.
                ans.append(-1)
                continue
            
            i = len(bin_lst) - 1
            while i > -1:
                print(i, bin_lst)
                if i == 0 and bin_lst[i] == "1":
                    bin_lst[0] = "0"
                    break
                
                if bin_lst[i] == "0":
                    bin_lst[i+1] = "0"
                    break

                i-=1
            
            if i == -1:
                ans.append(-1)
            else:
                ans.append(int("".join(bin_lst), 2))
        
        return ans
            
            
                
            

        