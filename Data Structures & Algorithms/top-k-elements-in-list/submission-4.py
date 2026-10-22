class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        h = []
        for nr in d.keys():
            heapq.heappush(h,(d[nr], nr))

            if len(h) > k:
              heapq.heappop(h)
        res = []
        for i in range(k):
            res.append(heapq.heappop(h)[1])
        return res

