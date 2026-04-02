class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp_s = {}
        mp_t = {}

        if len(s) != len(t):
            return False

        for char in s:
                mp_s[char] = 1 + mp_s.get(char, 1)
        
        for char in t:
                mp_t[char] = 1 + mp_t.get(char, 1)
        
        if mp_t == mp_s:
            return True
        else:
            return False