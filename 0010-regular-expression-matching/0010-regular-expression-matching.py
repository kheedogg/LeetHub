class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        import re
        ans = re.findall(p, s)
        for e in ans:
            if s == e:
                return True
        return False