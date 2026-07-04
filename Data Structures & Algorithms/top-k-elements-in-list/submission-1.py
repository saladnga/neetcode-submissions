class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        arr, res = [], []
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
        for num, freq in count.items():
            arr.append([freq, num])
        arr.sort()
        while len(res) < k:
            res.append(arr.pop()[1])
        return res