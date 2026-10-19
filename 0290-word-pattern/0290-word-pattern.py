class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()

        if len(pattern) != len(words):
            return False

        a = {}
        b = {}

        for i in range(len(pattern)):
            if pattern[i] in a and a[pattern[i]] != words[i]:
                return False

            if words[i] in b and b[words[i]] != pattern[i]:
                return False

            a[pattern[i]] = words[i]
            b[words[i]] = pattern[i]

        return True
