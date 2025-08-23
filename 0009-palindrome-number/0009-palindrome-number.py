class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False

        origin_str = str(x)
        for i in range(len(origin_str)//2):
            ii = len(origin_str) -1 - i
            e1, e2 = origin_str[i], origin_str[ii]
            if e1 == e2:
                continue
            else:
                return False
        return True