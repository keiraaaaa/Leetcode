#############################
# 8. String to Integer (atoi)
#############################
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        i = 0
        while i<len(str) and str[i]==" ":
            i += 1
        str = str[i:]
        if not str:
            return 0
        if str[0]=='-':
            if not str[1:] or not str[1].isnumeric(): return 0
            i = 1
            while i<len(str) and str[i].isnumeric():
                i += 1
            if int(str[:i])<-2**31: return -2**31
            else: return int(str[:i])
        if str[0].isnumeric():
            i = 0
            while i<len(str) and str[i].isnumeric():
                i += 1
            if int(str[:i])>2**31-1: return 2**31-1
            else: return int(str[:i])
        if str[0]=='+':
            if not str[1:] or not str[1].isnumeric(): return 0
            i = 1
            while i<len(str) and str[i].isnumeric():
                i += 1
            if int(str[:i])>2**31-1: return 2**31-1
            else: return int(str[:i])
        return 0


a = '+1'
solu = Solution()
print (solu.myAtoi(a))
# print (a[1].isnumeric())







