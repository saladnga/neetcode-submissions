class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash = {}
        if len(s) != len(t):
            return False
        for char in s:
            if char in hash:
                hash[char] += 1
            else:
                hash[char] = 1
        for char in t:
            if char not in hash:
                return False
            else:
                hash[char] -= 1
                if hash[char] < 0:
                    return False
        return True