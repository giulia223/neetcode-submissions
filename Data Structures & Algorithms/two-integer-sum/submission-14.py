class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx, nr in enumerate(nums):
            if target - nr in d.keys():
                return [ d[target - nr], idx]
            else: d[nr] = idx
        return [] 


