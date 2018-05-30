################
# 66. Plus One
################
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = digits[::-1]
        last = 1
        for i in range(len(digits)):
            digits[i], last = (digits[i] + last) % 10, int(digits[i]+last-10>=0)
            if i==len(digits)-1 and last==1:
                digits.append(1)
        return digits[::-1]

digits = []
solu = Solution()
print (solu.plusOne(digits))
