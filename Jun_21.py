'''
#####################################
# 394. Decode String
#####################################
class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        stack = []
        i, j = 0, 0
        for s_ in s:
            if s_=='[':
                i = j
                stack.append(s_)
                j += 1
            elif s_==']':
                print (stack,i,j)
                temp = ""
                k = j-1
                while stack[k]!='[':
                    temp = stack.pop() + temp
                    k -= 1
                stack.pop()
                k -= 1
                m = ""
                while k>=0 and str.isnumeric(stack[k]):
                    m = stack.pop() + m
                    k -= 1
                i = k+1
                # print (temp * int(m))
                stack.append(temp * int(m))
                j = i+1         
                while i>=0 and stack[i]!='[':
                    i -= 1
            else:
                stack.append(s_)
                j += 1
        return "".join(stack)

s = '3[a2[c]]'
s = '3[a]2[bc]'
s = '2[abc]3[cd]ef'
# s = '2[abc]'
solu = Solution()
print (solu.decodeString(s))
'''
'''
#####################################
# 406. Queue Reconstruction by Height
#####################################
class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if not people:
            return people
        sorted_people = sorted(sorted(people, key = lambda x: x[1]), key = lambda x: x[0], reverse=True)
        out = [sorted_people[0]]
        for i in range(1, len(sorted_people)):
            if sorted_people[i][1]==0:
                out = [sorted_people[i]]+ out
            else:
                out = out[:sorted_people[i][1]] + [sorted_people[i]] + out[sorted_people[i][1]:]
        return out

people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
solu = Solution()
print (solu.reconstructQueue(people))
'''

#####################################
# 416. Partition Equal Subset Sum
#####################################
class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums)==1:
            return False
        target = sum(nums)/2
        if target%1!=0:
            return False
        target = int(target)
        dp = [False] * (target+1)
        for j in range(len(nums)):
            for i in range(target, 0, -1):
                if dp[target]==True:
                    return True             
                if dp[i]==True and i+nums[j]<=target:
                    dp[i+nums[j]] = True 
            if nums[j]<=target:
                dp[nums[j]] = True         
        return False

nums = [100]
solu = Solution()
print (solu.canPartition(nums))














