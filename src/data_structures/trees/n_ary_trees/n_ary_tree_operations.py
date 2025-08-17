from ..tree_node import TreeNode
from typing import Any


def create_root(data: Any, children: list[TreeNode] | None = None) -> TreeNode:
    """
    Create a root node for an n-ary tree with proper initialization.

    This function creates a new TreeNode with the provided data and marks it as
    the root of the tree. Optionally accepts a list of existing child nodes.

    Args:
        data (Any): The data to store in the root node
        children (list[TreeNode] | None): Optional list of existing child nodes

    Returns:
        TreeNode: The created root node with is_root=True and is_parent=True

    Example:
        >>> root = create_root("root_data")
        >>> print(root.is_root)  # True
        >>> print(root.data)  # "root_data"
    """
    root = TreeNode(data, parent=None, children_nodes=children or [])  # ✅ Ensure list
    root.is_root = True

    if children:  # ✅ Only set is_parent if there are actually children
        root.is_parent = True
        # Update parent references
        for child in children:
            child.parent = root

    return root


def create_root_with_children_data_list(
    data: Any, children_data_list: list[Any]
) -> TreeNode:
    """
    Create a root node and initialize it with child nodes from data list.

    This function creates a root node and automatically creates child nodes
    from the provided data list. Each data item becomes a child node.

    Args:
        data (Any): The data to store in the root node
        children_data_list (list[Any]): List of data items to create child nodes

    Returns:
        TreeNode: The created root node with children attached

    Note:
        Children nodes will have children_nodes=None, which may cause issues
        if further children are added later.

    Example:
        >>> root = create_root_with_children_data_list("root", ["child1", "child2"])
        >>> print(len(root.children_nodes))  # 2
        >>> print(root.children_nodes[0].data)  # "child1"
    """
    root = TreeNode(data, parent=None, children_nodes=[])
    root.is_root = True
    root.is_parent = True

    if children_data_list:
        for child_data in children_data_list:
            if child_data:
                child = TreeNode(child_data, root, [])  # ✅ Use [] instead of None
                root.children_nodes.append(child)

    return root


def create_root_with_children_nodes_list(
    data: Any, children_nodes_list: list[TreeNode] | None = None
) -> TreeNode:
    """
    Create a root node and attach existing TreeNode objects as children.

    This function creates a root node and attaches pre-existing TreeNode
    objects as its children, updating their parent references.

    Args:
        data (Any): The data to store in the root node
        children_nodes_list (list[TreeNode] | None): Optional list of existing
            TreeNode objects to attach as children

    Returns:
        TreeNode: The created root node with attached children

    Example:
        >>> child1 = TreeNode("child1")
        >>> child2 = TreeNode("child2")
        >>> root = create_root_with_children_nodes_list("root", [child1, child2])
        >>> print(root.children_nodes)  # [child1, child2]
        >>> print(child1.parent)  # root
    """
    root = TreeNode(data, parent=None, children_nodes=[])
    root.is_root = True
    root.is_parent = True

    if children_nodes_list:
        for child_node in children_nodes_list:
            if child_node:
                child_node.parent = root
                root.children_nodes.append(child_node)

    return root


def add_child_node(parent_node: TreeNode, child_node_data: Any) -> TreeNode | None:
    """
    Add a child node to a given parent node.

    This function creates a new TreeNode as a child of the specified parent node.
    The child node will not have any children_nodes initially.

    Args:
        parent_node (TreeNode): The parent node to add the child to
        child_node_data (Any): The data for the new child node

    Returns:
        TreeNode | None: The created child node, or None if child_node_data is None

    Example:
        >>> root = create_root("root")
        >>> child = add_child_node(root, "child1")
        >>> print(root.children_nodes)  # [child]
        >>> print(child.parent)  # root
    """
    if parent_node is None:
        raise ValueError("Parent node cannot be None")

    if parent_node.children_nodes is None:
        parent_node.children_nodes = []  # ✅ Initialize if None

    if child_node_data:
        child_node = TreeNode(child_node_data, parent=parent_node, children_nodes=[])
        parent_node.children_nodes.append(child_node)

        if not parent_node.is_parent:  # ✅ Update parent flag
            parent_node.is_parent = True

        return child_node

    return None


def add_child_nodes(
    parent_node: TreeNode, children_data: list[Any]
) -> list[TreeNode] | None:
    """
    Add multiple child nodes to a given parent node.

    This function creates new TreeNode objects for each item in the children_data
    list and adds them as children of the specified parent node.

    Args:
        parent_node (TreeNode): The parent node to add the children to
        children_data (list[Any]): The data for the new child nodes

    Returns:
        list[TreeNode] | None: A list of the created child nodes, or None if no children were added

    Example:
        >>> root = create_root("root")
        >>> children = add_child_nodes(root, ["child1", "child2"])
        >>> print(len(root.children_nodes))  # 2
        >>> print(children[0].parent)  # root
    """
    added_children = []

    for child_data in children_data:
        child_node = add_child_node(parent_node, child_data)
        added_children.append(child_node)

    return added_children if added_children else None


def add_child_node_at_index(
    parent_node: TreeNode, child_node_data: Any, index: int
) -> TreeNode | None:
    """
    Add a child node to a specific index of the parent's children list.

    This function creates a new TreeNode as a child of the specified parent node
    and inserts it at the given index. The index must be within the range of the
    current children_nodes list size.

    Args:
        parent_node (TreeNode): The parent node to add the child to
        child_node_data (Any): The data for the new child node
        index (int): The index at which to insert the new child node

    Returns:
        TreeNode | None: The created child node, or None if child_node_data is None or index is out of range

    Example:
        >>> root = create_root("root")
        >>> child = add_child_node_at_index(root, "child1", 0)
        >>> print(root.children_nodes)  # [child]
        >>> print(child.parent)  # root
    """
    if parent_node is None:
        raise ValueError("Parent node cannot be None")

    if parent_node.children_nodes is None:
        parent_node.children_nodes = []

    if child_node_data and (0 <= index <= len(parent_node.children_nodes)):
        child_node = TreeNode(child_node_data, parent=parent_node, children_nodes=[])
        parent_node.children_nodes.insert(index, child_node)

        if not parent_node.is_parent:
            parent_node.is_parent = True

        return child_node

    return None


def add_child_nodes_from_index(
    parent_node: TreeNode, children_nodes_data: Any, index: int
) -> list[TreeNode] | None:
    """
    Add multiple child nodes to a given parent node starting from a specific index.

    This function creates new TreeNode objects for each item in the children_nodes_data
    list and inserts them into the parent's children_nodes list starting at the given index.

    Args:
        parent_node (TreeNode): The parent node to add the children to
        children_nodes_data (Any): The data for the new child nodes
        index (int): The index at which to start inserting the new child nodes

    Returns:
        list[TreeNode] | None: A list of the created child nodes, or None if no children were added

    Example:
        >>> root = create_root("root")
        >>> children = add_child_nodes_from_index(root, ["child1", "child2"], 0)
        >>> print(len(root.children_nodes))  # 2
        >>> print(children[0].parent)  # root
    """
    if parent_node is None:
        raise ValueError("Parent node cannot be None")

    if parent_node.children_nodes is None:
        parent_node.children_nodes = []

    added_children = []

    if children_nodes_data and 0 <= index <= len(parent_node.children_nodes):
        count = index

        for child_node_data in children_nodes_data:
            child_node = TreeNode(
                child_node_data,
                parent=parent_node,
                children_nodes=[],  # ✅ Use [] instead of None
            )
            parent_node.children_nodes.insert(count, child_node)
            count += 1
            added_children.append(child_node)

        if not parent_node.is_parent:  # ✅ Update parent flag
            parent_node.is_parent = True

    return added_children if added_children else None


def pre_order_traversal(root: TreeNode, result: list[Any]) -> list[Any] | None:
    """
    Perform a pre-order traversal of the tree.

    This function traverses the tree in pre-order (root, children) and appends
    the data of each visited node to the result list.

    Args:
        root (TreeNode): The root of the tree to traverse
        result (list[Any]): The list to append the visited node data to

    Returns:
        list[Any] | None: The result list containing the pre-order traversal,
            or None if the tree is empty

    Example:
        >>> root = create_root("root", ["child1", "child2"])
        >>> result = pre_order_traversal(root, [])
        >>> print(result)  # ["root", "child1", "child2"]
    """
    if root is None:
        return None

    result.append(root.data)

    if root.children_nodes:  # ✅ Check for None and non-empty
        for child in root.children_nodes:
            pre_order_traversal(child, result)  # ✅ No reassignment needed

    return result


def post_order_traversal(root: TreeNode, result: list[Any]) -> list[Any] | None:
    """
    Perform a post-order traversal of the tree.

    This function traverses the tree in post-order (children, root) and appends
    the data of each visited node to the result list.

    Args:
        root (TreeNode): The root of the tree to traverse
        result (list[Any]): The list to append the visited node data to

    Returns:
        list[Any] | None: The result list containing the post-order traversal,
            or None if the tree is empty

    Example:
        >>> root = create_root("root", ["child1", "child2"])
        >>> result = post_order_traversal(root, [])
        >>> print(result)  # ["child1", "child2", "root"]
    """
    if root is None:
        return None

    if root.children_nodes:  # ✅ Check for None and non-empty
        for child in root.children_nodes:
            post_order_traversal(child, result)

    result.append(root.data)
    return result  # ✅ Always return result


def level_order_traversal(root: TreeNode, result: list[Any]) -> list[Any] | None:
    """
    Perform a level-order traversal of the tree.

    This function traverses the tree level by level (breadth-first) and appends
    the data of each visited node to the result list.

    Args:
        root (TreeNode): The root of the tree to traverse
        result (list[Any]): The list to append the visited node data to

    Returns:
        list[Any] | None: The result list containing the level-order traversal,
            or None if the tree is empty

    Example:
        >>> root = create_root("root", ["child1", "child2"])
        >>> result = level_order_traversal(root, [])
        >>> print(result)  # ["root", "child1", "child2"]
    """
    if root is None:
        return None
    else:
        queue = [root]

        while queue:
            current = queue.pop(0)
            result.append(current.data)

            for child in current.children_nodes:
                queue.append(child)

    return result


def breadth_first_search(root: TreeNode, target: Any) -> TreeNode | None:
    """
    Perform a breadth-first search for a target value in the tree.

    This function searches for a node with the specified target value using
    breadth-first search. Returns the first matching node found.

    Args:
        root (TreeNode): The root of the tree to search
        target (Any): The target value to search for

    Returns:
        TreeNode | None: The first node matching the target value, or None if not found

    Example:
        >>> root = create_root("root", ["child1", "child2"])
        >>> result = breadth_first_search(root, "child2")
        >>> print(result.data)  # "child2"
    """
    if root is None:
        return None
    elif root.children_nodes is None:
        if root.data == target:
            return root
        else:
            return None
    else:
        queue = [root]

        while queue:
            current = queue.pop(0)

            if current.data == target:
                return current
            else:
                for child in current.children_nodes:
                    queue.append(child)

    return None


def depth_first_search(root: TreeNode, target: Any) -> TreeNode | None:
    """
    Perform a depth-first search for a target value in the tree.

    This function searches for a node with the specified target value using
    depth-first search. Returns the first matching node found.

    Args:
        root (TreeNode): The root of the tree to search
        target (Any): The target value to search for

    Returns:
        TreeNode | None: The first node matching the target value, or None if not found

    Example:
        >>> root = create_root("root", ["child1", "child2"])
        >>> result = depth_first_search(root, "child2")
        >>> print(result.data)  # "child2"
    """
    if root is None:
        return None
    elif root.children_nodes is None:
        if root.data == target:
            return root
        else:
            return None
    else:
        if root.data == target:
            return root
        else:
            for child in root.children_nodes:
                result = depth_first_search(child, target)

                if result is not None:
                    return result

    return None


def search_and_remove_node(root: TreeNode, target: Any) -> TreeNode | None:
    """
    Search for a node by value and remove it from the tree.

    This function searches for a node with the specified target value, removes
    it from the tree, and returns the removed node. The removed node's children
    are reattached to the parent of the removed node.

    Args:
        root (TreeNode): The root of the tree to search
        target (Any): The target value to search for and remove

    Returns:
        TreeNode | None: The removed node, or None if not found or if it's the root node

    Example:
        >>> root = create_root("root", ["child1", "child2"])
        >>> removed_node = search_and_remove_node(root, "child1")
        >>> print(removed_node.data)  # "child1"
        >>> print(root.children_nodes)  # [child2]
    """
    if root is None:
        return None

    result = depth_first_search(root, target)

    if result is not None and result.parent is not None:
        # Save children before clearing references
        children_to_move = result.children_nodes.copy() if result.children_nodes else []

        # Update parent references for children
        for child in children_to_move:
            child.parent = result.parent

        # Remove node from parent
        result.parent.children_nodes.remove(result)

        # Add children to parent (ensure parent has children_nodes list)
        if result.parent.children_nodes is None:
            result.parent.children_nodes = []
        result.parent.children_nodes.extend(children_to_move)

        # Clean up removed node
        result.parent = None
        result.children_nodes = []
        return result

    return None


def search_and_remove_nodes(
    root: TreeNode, targets: list[Any]
) -> list[TreeNode] | None:
    """
    Search for multiple nodes by value and remove them from the tree.

    This function searches for nodes with the specified target values, removes
    them from the tree, and returns a list of the removed nodes. The removed nodes'
    children are reattached to the parents of the removed nodes.

    Args:
        root (TreeNode): The root of the tree to search
        targets (list[Any]): The list of target values to search for and remove

    Returns:
        list[TreeNode] | None: A list of the removed nodes, or None if none were found or if all are root nodes

    Example:
        >>> root = create_root("root", ["child1", "child2", "child3"])
        >>> removed_nodes = search_and_remove_nodes(root, ["child1", "child3"])
        >>> print(len(removed_nodes))  # 2
        >>> print(root.children_nodes)  # [child2]
    """
    if root is None or not targets:
        return None

    removed_nodes = []

    for target in targets:
        # ✅ Use the corrected single removal function
        removed_node = search_and_remove_node(root, target)
        if removed_node is not None:
            removed_nodes.append(removed_node)

    return removed_nodes if removed_nodes else None
