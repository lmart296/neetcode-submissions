class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = Counter(s)
        
        for c in t:
            if c in m:
                m[c] = m[c] - 1
                if m[c] == 0:
                    del m[c]
            else:
                return False
        
        return not m
