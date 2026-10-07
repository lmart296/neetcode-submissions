class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        maxcount = count = 0
        seen = set()
        while r < len(s):
            if s[r] not in seen:
                count += 1
                seen.add(s[r])
                r+=1
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    count -= 1
                    l += 1
                seen.add(s[r])
                count+=1
                r+=1
            maxcount = max(maxcount, count)
        return maxcount