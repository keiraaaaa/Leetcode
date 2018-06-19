'''
########################
# 207. Course Schedule
########################
class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for i in range (numCourses)]
        visit = [0 for i in range (numCourses)]
        for x,y in prerequisites:
            graph[x].append(y)
        for i in range(numCourses):
            if visit[i]!=1:
                if not self.dfs(graph, visit, i):
                    return False
        return True
        
    def dfs(self, graph, visit, i):
        if visit[i]==-1:
            return False
        if visit[i]==1:
            return True
        visit[i] = -1
        for j in graph[i]:
            if not self.dfs(graph, visit, j):
                return False
        visit[i] = 1
        return True
        




numCourses = 2
prerequisites = [[1,0],[0,1]]
# numCourses = 4
# prerequisites = [[0,1],[0,2],[0,3],[1,3],[3,2]]
# numCourses = 2
# prerequisites = [[0,1]]
solu = Solution()
print (solu.canFinish(numCourses, prerequisites))
'''

#####################################
# 208. Implement Trie (Prefix Tree)
#####################################
class TrieNode:
    def __init__(self):
        self.words = False
        self.children = {}

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for i in range(len(word)):
            if word[i] not in node.children:
                node.children[word[i]] = TrieNode()
            node = node.children[word[i]]
        node.words = True
        # print (self.root.children['a'].children)

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for i in range (len(word)):
            if word[i] not in node.children:
                return False
            node = node.children[word[i]]
        if node.words==False:
            return False
        return True


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for i in range (len(prefix)):
            if prefix[i] not in node.children:
                return False
            node = node.children[prefix[i]]
        return True   
               

# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
print (obj.search("app"))
print (obj.startsWith("app"))

# obj.insert("app")
# print (obj.search("app"))
# param_3 = obj.startsWith(prefix)






















