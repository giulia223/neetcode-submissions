class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = Counter(nums)
        for cnt in dic.values():
            if cnt > 1: return True
        return False