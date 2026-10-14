class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        hash_set = set()
        max_length = 0

        for right in range(len(s)):
            while s[right] in hash_set:
                hash_set.remove(s[left])
                left += 1

            hash_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length
        # if len(s) <= 1:
        #     return len(s)
        # max_counter = 0
        # for i in range(len(s)):
        #     hash_set = {s[i]}
        #     counter = 1
        #     for j in range(i+1, len(s)):
        #         if s[j] in hash_set:
        #             max_counter = counter if counter > max_counter else max_counter
        #             break
        #         else:
        #             counter += 1
        #             hash_set.add(s[j])
        #     max_counter = counter if counter > max_counter else max_counter
        # return max_counter

