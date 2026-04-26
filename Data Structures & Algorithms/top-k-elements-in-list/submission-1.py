class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = []
        counter = Counter(nums)

        for n in counter.keys():
            heapq.heappush(h, (counter[n], n))
            if len(h) > k:
                heapq.heappop(h)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(h)[1])
        return res
