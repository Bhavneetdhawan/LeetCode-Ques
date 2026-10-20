class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        sa = sum(aliceSizes)
        sb = sum(bobSizes)
        diff = (sb - sa) // 2

        s = set(bobSizes)

        for a in aliceSizes:
            if a + diff in s:
                return [a, a + diff]