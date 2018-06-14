###################
# 139. Word Break
###################
'''
class Solution:
    def check(self, temp, n, wordDict):
        if n>=len(wordDict):
            return True
        if len(temp)<len(wordDict[n]):
            return False
        i = 0
        result = False
        # print (temp, wordDict[n])
        while i<=len(temp)-len(wordDict[n]):
            if temp[i:i+len(wordDict[n])]==wordDict[n]:
                # print (temp[i:i+len(wordDict[n])], wordDict[n])
                result = result or self.check(temp[:i]+temp[i+len(wordDict[n]):], n+1, wordDict) 
            i += 1
        return result


    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if s and wordDict==[]:
            return False
        return self.check(s, 0, wordDict)
'''
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        d = [False] * len(s)    
        for i in range(len(s)):
            for w in wordDict:
                if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
                    d[i] = True
        return d[-1] 



# s = "applepenapple"
# wordDict = ["apple", "pen"]
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# s = "leetcode"
# wordDict = ["leet", "code"]
# s = "a"
# wordDict = []
s = "catsandog"
wordDict = ["cat",  "dog", "cats", "an" ]
solu = Solution()
print (solu.wordBreak(s, wordDict))
