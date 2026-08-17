class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        u_types=len(set(candyType))
        return min(u_types,len(candyType)//2)