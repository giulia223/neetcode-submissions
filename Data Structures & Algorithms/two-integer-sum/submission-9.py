class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx, i in enumerate(nums):
            print(i)
            if target - i in d.keys():
                return [ d[target - i], idx]
            else: d[i]  = idx
        print(d)
        return []