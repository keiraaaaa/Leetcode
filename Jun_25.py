#############################
# 29. Divide Two Integers
#############################
class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend==-2**31 and divisor==-1:
            return 2**31-1
        if (dividend>0 and divisor<0) or (dividend<0 and divisor>0):
            sign = -1
        if (dividend>0 and divisor>0) or (dividend<0 and divisor<0):
            sign = 1
        dvd, dvs = abs(dividend), abs(divisor)
        if dvd<dvs:
            return 0
        res = 0
        while dvd>=dvs:
            temp, out = dvs, 1
            while dvd>=(temp<<1):
                temp <<= 1
                out <<= 1
            dvd -= temp
            res += out
        return res if sign==1 else -res

# dividend = 10
# divisor = 3
# dividend = 7
# divisor = -3
dividend = 1
divisor = 2
# dividend = 2147483647
# divisor = 1
dividend = 1036963541
divisor = -24409858
solu = Solution()
print (solu.divide(dividend, divisor))
