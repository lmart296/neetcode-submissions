class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = Counter(nums)
        res = []
        freq = [[] for i in range(len(nums) + 1)]
        for num, v in m.items():
            freq[v].append(num)
        
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

