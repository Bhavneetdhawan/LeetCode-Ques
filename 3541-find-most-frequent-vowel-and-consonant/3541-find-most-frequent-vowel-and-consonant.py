class Solution(object):
    def maxFreqSum(self, s):
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        v = 0
        c = 0

        for i in range(26):
            if chr(i + 97) in "aeiou":
                v = max(v, freq[i])
            else:
                c = max(c, freq[i])

        return v + c