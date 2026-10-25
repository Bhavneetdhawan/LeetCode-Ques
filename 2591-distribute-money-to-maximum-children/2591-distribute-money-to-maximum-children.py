class Solution(object):
    def distMoney(self, money, children):
        """
        :type money: int
        :type children: int
        :rtype: int
        """
        if money < children:
            return -1

        money -= children
        ans = min(money // 7, children)

        money -= ans * 7
        children -= ans

        if children == 0 and money > 0:
            ans -= 1

        if children == 1 and money == 3:
            ans -= 1

        return ans