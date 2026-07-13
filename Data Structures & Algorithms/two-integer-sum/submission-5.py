class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            print( i , n)
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], i ]
            hashmap[n] = i