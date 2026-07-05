class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        s1_count = [0] * 26
        window_count = [0] * 26

        for i in range(n1):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1

        matches = sum(1 for i in range(26) if s1_count[i] == window_count[i])

        left = 0
        for right in range(n1, n2):
            if matches == 26:
                return True

            add_char = ord(s2[right]) - ord('a')
            window_count[add_char] += 1
            if window_count[add_char] == s1_count[add_char]:
                matches += 1
            elif window_count[add_char] == s1_count[add_char] + 1:
                matches -= 1

            remove_char = ord(s2[left]) - ord('a')
            window_count[remove_char] -= 1
            if window_count[remove_char] == s1_count[remove_char]:
                matches += 1
            elif window_count[remove_char] == s1_count[remove_char] - 1:
                matches -= 1

            left += 1

        return matches == 26