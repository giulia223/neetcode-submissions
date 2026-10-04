class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for c in counter.values():
            if c > 1:
                return True
        return False