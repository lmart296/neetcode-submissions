class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}

        for s in strs:
            sortedS = ''.join(sorted(s))
            if sortedS not in m:
                m[sortedS] = []
            m[sortedS].append(s)
        
        return list(m.values())

        
        
                    