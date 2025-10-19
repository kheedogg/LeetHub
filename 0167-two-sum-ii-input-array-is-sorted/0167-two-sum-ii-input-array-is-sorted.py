class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        from collections import Counter
        freq = Counter(numbers)
        ans = []
        for k, v in freq.items():
            if v>=2:
                if k*2 == target:
                    for i, e in enumerate(numbers):
                        if e==k:
                            ans.append(i+1)
                        if len(ans) == 2:
                            return ans

        uniq_numbers = list(set(numbers))
        print(uniq_numbers)
        for i in range(len(uniq_numbers)-1):
            for j in range(i+1, len(uniq_numbers)):
                if uniq_numbers[i] + uniq_numbers[j] == target:
                    print(i, j, uniq_numbers[i], uniq_numbers[j])
                    n1, n2 = uniq_numbers[i], uniq_numbers[j]
        
                    return [min(numbers.index(n1)+1, numbers.index(n2)+1),
        max(numbers.index(n1)+1, numbers.index(n2)+1)]