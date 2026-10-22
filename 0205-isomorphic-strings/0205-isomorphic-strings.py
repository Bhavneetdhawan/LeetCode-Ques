class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a = {}
        b = {}

        for i in range(len(s)):
            if s[i] in a and a[s[i]] != t[i]:
                return False
            if t[i] in b and b[t[i]] != s[i]:
                return False

            a[s[i]] = t[i]
            b[t[i]] = s[i]

        return True