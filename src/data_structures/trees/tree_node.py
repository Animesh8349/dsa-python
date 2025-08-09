class TreeNode:
    def _init_(self, children: list | None = None):
        self.children = children
        self.isParent = False
        self.isRoot = False
        self.isLeaf = False
        self.isLeft = False
        self.isRight = False


class BinaryTreeNode:
    def __init__(self, leftChild: "BinaryTreeNode | None" = None, rightChild: "BinaryTreeNode | None" = None):
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.isRight = False
        self.isLeft = False
        self.isRoot = False
        self.isParent = False
        self.isLeaf = False
