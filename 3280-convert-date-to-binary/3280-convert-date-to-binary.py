class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:10])

        return bin(year)[2:] + "-" + bin(month)[2:] + "-" + bin(day)[2:]