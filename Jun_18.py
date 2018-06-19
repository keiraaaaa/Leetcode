'''
########################################
# 215. Kth Largest Element in an Array
########################################
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ######### My method #########
        # return sorted(nums)[-k]
        ######### Heap #########
        # import heapq
        # heap = []
        # for num in nums:
        #     heapq.heappush(heap, num)
        # for _ in range(len(nums)-k):
        #     heapq.heappop(heap)
        # return heapq.heappop(heap)
        ######### Quick Selection #########
        if nums:
            return self.findKthSmallest(nums, len(nums)-k)

    def findKthSmallest(self, nums, k):
        p = self.partition(nums, 0, len(nums)-1)
        # print (p,k, nums[p])
        if p<k:
            return self.findKthSmallest(nums[p+1:], k-p-1)
        if p>k:
            return self.findKthSmallest(nums[:p], k)
        return nums[p]

    def partition(self, nums, l, r):
        low = l
        while l<r:
            if nums[l]<nums[r]:
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low],nums[r] = nums[r],nums[low]
        return low

nums = [3,2,1,5,6,4]
k = 2
solu = Solution()
# solu.findKthLargest(nums, k)
print (solu.findKthLargest(nums, k))
'''
'''
#######################
# 221. Maximal Square
#######################
class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            size = 0
            return size
        status = [[0] * len(matrix[0]) for i in range (len(matrix))]
        maxsize = 0
        for i in range (len(matrix)):
            for j in range (len(matrix[0])):
                if i==0 or j==0:
                    status[i][j] = int(matrix[i][j])
                    maxsize = max(maxsize, status[i][j])
                else:
                    if int(matrix[i][j])==0:
                        status[i][j] = 0
                    else:
                        status[i][j] = min(status[i-1][j-1], status[i-1][j], status[i][j-1]) + 1
                        maxsize = max(maxsize, status[i][j])
        return maxsize**2

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
matrix = [["0","0"],["0","0"]]
matrix = [["1","1","1","1"],["1","1","1","1"],["1","1","1","1"]]
matrix = [["1","0","1","0"],["1","0","1","1"],["1","0","1","1"],["1","1","1","1"]]
solu = Solution()
print (solu.maximalSquare(matrix))
'''

##############################################
# 236. Lowest Common Ancestor of a Binary Tree
##############################################
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        stack = [root]
        Parent = {root: None}
        while p not in Parent or q not in Parent:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
                Parent[node.left] = node
            if node.right:
                stack.append(node.right)
                Parent[node.right] = node
        Ancestor = []
        while p:
            Ancestor.append(p)
            p = Parent[p]
        while q not in Ancestor:
            q = Parent[q]
        return q







root = TreeNode(3)
root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
p = root.left
q = root.right
solu = Solution()
print (solu.lowestCommonAncestor(root, p, q).val)










