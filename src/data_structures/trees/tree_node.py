from typing import Any


class TreeNode:
    def __init__(
        self,
        data: Any,
        parent: "TreeNode | None" = None,
        children_nodes: "list[TreeNode] | None" = None,
    ):
        self.data = data
        self.parent = parent
        self.children_nodes = children_nodes if children_nodes is not None else []
        self.is_root = False
        self.is_parent = False
        self.is_left = False
        self.is_right = False
        self.is_leaf = False


class BinaryTreeNode:
    def __init__(
        self,
        data: Any,
        parent: "BinaryTreeNode | None" = None,
        left_child: "BinaryTreeNode | None" = None,
        right_child: "BinaryTreeNode | None" = None,
    ):
        self.data = data
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child
        self.is_root = False
        self.is_parent = False
        self.is_left = False
        self.is_right = False
        self.is_leaf = False


class TernaryTreeNode:
    def __init__(
        self,
        data: Any,
        parent: "TernaryTreeNode | None" = None,
        left_child: "TernaryTreeNode | None" = None,
        middle_child: "TernaryTreeNode | None" = None,
        right_child: "TernaryTreeNode | None" = None,
    ):
        self.data = data
        self.parent = parent
        self.left_child = left_child
        self.middle_child = middle_child
        self.right_child = right_child
        self.is_root = False
        self.is_parent = False
        self.is_left = False
        self.is_middle = False
        self.is_right = False
        self.is_leaf = False
