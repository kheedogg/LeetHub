class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        lst = []
        for n in nums:
            if n<0:
                n = value - abs(n)%value
                n = n%value
            elif n>0:
                while n>=value:
                    n = n%value
            lst.append(n)
        
        from collections import Counter
        freq = Counter(lst)

        for n in range(value):
            if n not in freq:
                return n
        
        min_num = min(freq.values())

        flag = 0
        sorted_keys = sorted(freq.keys())
        for k in sorted_keys:
            v = freq[k] - min_num

            if v == 0:
                return value * min_num + k