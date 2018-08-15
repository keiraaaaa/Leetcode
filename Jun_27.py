'''
# Quicksort
def partition(arr, low ,high):
    pivot = arr[high]
    j = low
    for i in range (low, high):
        if arr[i]<=pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    arr[j], arr[high] = arr[high], arr[j]
    print(arr)
    return j

def quicksort(arr, low, high):
    if low<high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi-1)
        quicksort(arr, pi+1, high)
arr = [12]
n = len(arr)
quicksort(arr,0,n-1)
print (arr)
'''

####################
# 91. Decode Ways
####################
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0]=='0': return 0
        count, cur, prev = 1, 1, 1
        for i in range (1, len(s)):
            if int(s[i])>0 and int(s[i-1])*10+int(s[i])<=26:
                if int(s[i-1])*10+int(s[i])<10:
                    count = cur
                    prev = cur
                if int(s[i-1])*10+int(s[i])>=10:
                    count += prev
                    prev = cur
                    cur = count
            if int(s[i])>0 and int(s[i-1])*10+int(s[i])>26:
                    count = cur
                    prev = cur            
            if int(s[i])==0 and int(s[i-1])*10+int(s[i])<=26:
                count = prev
                cur = count
                prev = cur
            if (int(s[i])==0 and int(s[i-1])*10+int(s[i])>26) or int(s[i-1])*10+int(s[i])==0:
                return 0
            # print (cur, prev, s[i])
        return count

s = "24726"        
solu = Solution()
print (solu.numDecodings(s))














