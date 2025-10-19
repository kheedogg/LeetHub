class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        while len(s) > 1:
            if s[0] == s[-1]:
                s = s[1:-1]
            else:
                return False
        return True
