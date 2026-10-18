
class Solution(object):
    def restoreIpAddresses(self, s):
        ans = []
        n = len(s)

        for i in range(1, 4):
            for j in range(i + 1, i + 4):
                for k in range(j + 1, j + 4):
                    a = s[:i]
                    b = s[i:j]
                    c = s[j:k]
                    d = s[k:]

                    parts = [a, b, c, d]

                    if all(x != "" and len(x) <= 3 and
                           (x == "0" or x[0] != "0") and
                           int(x) <= 255 for x in parts):
                        if len(a) + len(b) + len(c) + len(d) == n:
                            ans.append(".".join(parts))

        return ans
