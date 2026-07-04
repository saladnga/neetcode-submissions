class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        i = 0
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
        return sorted(count, key=count.get, reverse=True)[:k]