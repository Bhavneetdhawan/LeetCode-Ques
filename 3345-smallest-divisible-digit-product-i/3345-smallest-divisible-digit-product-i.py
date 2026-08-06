class Solution(object):
    def smallestNumber(self, n, t):
        while True:
            p = 1

            for x in str(n):
                p *= int(x)

            if p % t == 0:
                return n

            n += 1