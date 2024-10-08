class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for n in nums:
            if count.get(n, 0) > 0:
                return True
            else:
                count[n] = count.get(n, 0) + 1
        return False