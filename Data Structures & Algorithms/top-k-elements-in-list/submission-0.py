class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range (len(nums) + 1)]

        for word in nums:
            count[word] = count.get(word, 0) + 1
        for c , n in count.items():
            freq[n].append(c)
        res = []
        for i  in range(len(freq) -1 ,0, -1):
            for num in freq[i]:
                res.append(num) 
            if k == len(res):
                return res

        