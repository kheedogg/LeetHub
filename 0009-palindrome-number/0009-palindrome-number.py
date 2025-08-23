class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False

        reverse_str = ''
        origin_str = str(x)
        for i in range(-1, -len(origin_str)-1, -1):
            reverse_str += origin_str[i]
        
        if reverse_str == origin_str:
            return True
        else:
            return False
        