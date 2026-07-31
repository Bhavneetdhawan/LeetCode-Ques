class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        """
        :type nums: List[int]
        :type digit: int
        :rtype: int
        """
        count = 0
        d = str(digit)

        for num in nums:
            count += str(num).count(d)

        return count