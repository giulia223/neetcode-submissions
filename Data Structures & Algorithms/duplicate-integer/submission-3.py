class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        print(counter)
        for i in counter.values():
            if i >= 2 :
                 return True
        return False