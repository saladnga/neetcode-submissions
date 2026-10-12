class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time Complexity: O(N + M)
        # Space Complexity: O(1)

        if len(s) != len(t):
            return False
        
        count = {}
        for char1 in s:
            if char1 not in count:
                count[char1] = 1
            else:
                count[char1] += 1
        for char2 in t:
            if char2 not in count:
                return False
            else:
                count[char2] -= 1
        
        for val in count.values():
            if val != 0:
                return False

        return True