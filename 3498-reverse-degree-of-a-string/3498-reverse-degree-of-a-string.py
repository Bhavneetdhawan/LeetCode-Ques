class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0

        for i, ch in enumerate(s, start=1):
            reverse_pos = ord('z') - ord(ch) + 1
            total += reverse_pos * i

        return total