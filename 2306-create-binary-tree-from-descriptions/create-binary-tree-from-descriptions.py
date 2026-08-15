# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        dic={}
        
        for ele1,ele2,_ in descriptions:
            if ele1 not in dic:
                dic[ele1] = TreeNode(ele1)
            if ele2 not in dic:
                dic[ele2] = TreeNode(ele2)
        sett = set(dic.keys())
        for parent,child,isLeftChild in descriptions:
            if isLeftChild:
                dic[parent].left = dic[child]
            else:
                dic[parent].right = dic[child]
            if child in sett:
                sett.remove(child)
        return dic[sett.pop()]
        