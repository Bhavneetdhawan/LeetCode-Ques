class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        mp = {}
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        j = 0

        for ch in key:
            if ch != ' ' and ch not in mp:
                mp[ch] = alphabet[j]
                j += 1

        ans = ""

        for ch in message:
            if ch == ' ':
                ans += ' '
            else:
                ans += mp[ch]

        return ans