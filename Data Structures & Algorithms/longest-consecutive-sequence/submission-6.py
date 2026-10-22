class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxi = 0
        for n in numset:
            if n - 1 not in numset:
                len = 1
                while n + len in numset:
                    len = len + 1
                maxi = max(maxi, len)
        return maxi
            