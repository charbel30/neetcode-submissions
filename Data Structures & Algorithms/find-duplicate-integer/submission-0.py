class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = 1+ count.get(nums[i],0)
        maxi = max(count , key= count.get)
        print(count)
        print(maxi)
        return maxi