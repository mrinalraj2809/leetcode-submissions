class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        i = 0
        hashm_s1 = [0] *26

        hashm_s2 = [0] *26
        for c in s1:
            hashm_s1[ord(c) - ord('a')] = hashm_s1[ord(c) - ord('a')] + 1
        while i < len(s2):
            flag = 0
            hashm_wind = [0] * 26
            for c in s2[i: i + window]:
                # print(c)
                if c not in s1:
                    break
                hashm_wind[ord(c) - ord('a')] = hashm_wind[ord(c) - ord('a')] + 1
            if hashm_wind == hashm_s1:
                return True
            i += 1
        return False