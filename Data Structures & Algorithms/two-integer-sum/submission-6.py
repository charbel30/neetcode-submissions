class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i , n in enumerate(nums):
            total = target - n
            if total in hashmap:
                return [hashmap[total], i]
            hashmap[n] = i
