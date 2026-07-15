class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            curr = -1
            for j in range(i + 1, len(arr)):
                curr = max(curr, arr[j])
            arr[i] = curr
        arr[len(arr) - 1] = -1
        return arr