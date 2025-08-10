from data_structures.trees.tree_node import TreeNode
from typing import Any


def create_root(self, data: Any, children: list[Any] | None = None) -> TreeNode:
    root = TreeNode(data, children)
    root.is_root = True
    root.is_parent = True
    return root


def create_root_with_children_data_list(
    self, data: Any, children_data_list: list[Any]
) -> TreeNode:
    root = TreeNode(data, None)
    root.is_root = True
    root.is_parent = True

    if children_data_list:
        for child_data in children_data_list:
            if child_data:
                child = TreeNode(child_data, None)
                root.children_nodes.append(child)

    return root


def create_root_with_children_nodes_list(
    self, data: Any, children_nodes_list: list[TreeNode] | None = None
) -> TreeNode:
    root = TreeNode(data, None)
    root.is_root = True
    root.is_parent = True

    if children_nodes_list:
        for child_node in children_nodes_list:
            if child_node:
                root.children_nodes.append(child_node)

    return root


def add_child_node(
    self, parent_node: TreeNode, child_node_data: Any
) -> TreeNode | None:
    child_node = None

    if child_node_data:
        child_node = TreeNode(child_node_data, None)
        parent_node.children_nodes.append(child_node)

    return child_node


def add_child_nodes(
    self, parent_node: TreeNode, children_data: list[Any]
) -> list[TreeNode] | None:
    added_children = []

    for child_data in children_data:
        child_node = self.add_child_node(parent_node, child_data)
        added_children.append(child_node)

    return added_children if added_children else None


def add_child_node_at_index(
    self, parent_node: TreeNode, child_node_data: Any, index: int
) -> TreeNode | None:
    child_node = None

    if child_node_data and (0 <= index <= len(parent_node.children_nodes)):
        child_node = TreeNode(child_node_data, None)
        parent_node.children_nodes.insert(index, child_node)

    return child_node


def add_child_nodes_from_index(
    self, parent_node: TreeNode, children_nodes_data: Any, index: int
) -> list[TreeNode] | None:
    child_node = None
    added_children = []

    if children_nodes_data and 0 <= index <= len(parent_node.children_nodes):
        count = index

        for child_node_data in children_nodes_data:
            child_node = TreeNode(child_node_data, None)
            parent_node.children_nodes.insert(count, child_node)
            count += 1
            added_children.append(child_node)

    return added_children if added_children else None
