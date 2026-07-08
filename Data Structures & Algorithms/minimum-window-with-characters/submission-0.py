from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        
        t_count = Counter(t)
        window_count = {}
        have = 0
        need = len(t_count)
        result = ""
        result_len = float("infinity")
        left = 0
        
        for right in range(len(s)):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1
            
            if char in t_count and window_count[char] == t_count[char]:
                have += 1
            
            while have == need:
                if right - left + 1 < result_len:
                    result_len = right - left + 1
                    result = s[left:right+1]
                window_count[s[left]] -= 1
                if s[left] in t_count and window_count[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1
        
        return result
        