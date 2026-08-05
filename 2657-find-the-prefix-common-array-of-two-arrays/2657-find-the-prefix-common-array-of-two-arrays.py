class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        ans = []

        for i in range(len(A)):
            count = 0

            for num in range(1, len(A) + 1):
                if num in A[:i+1] and num in B[:i+1]:
                    count += 1

            ans.append(count)

        return ans