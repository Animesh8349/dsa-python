# test_nary_tree.py
import pytest

from ...src.data_structures.trees.n_ary_trees.n_ary_tree_operations import (
    TreeNode,
    create_root,
    create_root_with_children_data_list,
    create_root_with_children_nodes_list,
    add_child_node,
    add_child_nodes,
    add_child_node_at_index,
    add_child_nodes_from_index,
    pre_order_traversal,
    post_order_traversal,
    level_order_traversal,
    breadth_first_search,
    depth_first_search,
    search_and_remove_node,
    search_and_remove_nodes,
)

# ---------------------------
# Helpers & Fixtures
# ---------------------------


@pytest.fixture
def simple_root():
    return create_root("root")


@pytest.fixture
def root_with_children_data():
    # root: A, children: B, C, D
    root = create_root_with_children_data_list("A", ["B", "C", "D"])
    return root


@pytest.fixture
def root_with_nested_tree():
    # A -> [B, C, D]
    # B -> [E, F]
    # C -> []
    # D -> [G]
    root = create_root_with_children_data_list("A", ["B", "C", "D"])
    b = root.children_nodes[0]
    d = root.children_nodes[2]
    add_child_nodes(b, ["E", "F"])
    add_child_node(d, "G")
    return root


def children_data_list(node):
    return [c.data for c in (node.children_nodes or [])]


# ---------------------------
# create_root
# ---------------------------


def test_create_root_without_children_flags(simple_root):
    root = simple_root
    assert root.data == "root"
    assert root.is_root is True
    # If no children passed, is_parent should remain default/False unless your class defaults True.
    assert getattr(root, "is_parent", False) is False
    assert root.parent is None
    assert isinstance(root.children_nodes, list)
    assert root.children_nodes == []


def test_create_root_with_children_sets_parents_and_flags():
    c1, c2 = TreeNode("c1"), TreeNode("c2")
    root = create_root("R", [c1, c2])
    assert root.is_root is True
    assert root.is_parent is True
    assert c1.parent is root and c2.parent is root
    assert children_data_list(root) == ["c1", "c2"]


# ---------------------------
# create_root_with_children_data_list
# ---------------------------


def test_create_root_with_children_data_list_creates_children():
    root = create_root_with_children_data_list("R", ["a", "b", "c"])
    assert root.is_root is True
    assert root.is_parent is True
    assert children_data_list(root) == ["a", "b", "c"]
    for child in root.children_nodes:
        assert child.parent is root
        assert child.children_nodes == []


def test_create_root_with_children_data_list_ignores_falsy():
    root = create_root_with_children_data_list("R", ["x", None, "", "y"])
    assert children_data_list(root) == ["x", "y"]


# ---------------------------
# create_root_with_children_nodes_list
# ---------------------------


def test_create_root_with_children_nodes_list_attaches_and_updates_parents():
    c1, c2 = TreeNode("c1"), TreeNode("c2")
    root = create_root_with_children_nodes_list("R", [c1, c2])
    assert root.is_root is True
    assert root.is_parent is True
    assert children_data_list(root) == ["c1", "c2"]
    assert c1.parent is root and c2.parent is root


def test_create_root_with_children_nodes_list_ignores_none_entries():
    c1 = TreeNode("c1")
    root = create_root_with_children_nodes_list("R", [c1, None])
    assert children_data_list(root) == ["c1"]


# ---------------------------
# add_child_node / add_child_nodes
# ---------------------------


def test_add_child_node_sets_parent_and_flag(simple_root):
    root = simple_root
    assert getattr(root, "is_parent", False) is False
    child = add_child_node(root, "c1")
    assert child is not None
    assert child.parent is root
    assert children_data_list(root) == ["c1"]
    assert root.is_parent is True


def test_add_child_node_none_data_returns_none(simple_root):
    assert add_child_node(simple_root, None) is None
    assert simple_root.children_nodes == []


def test_add_child_node_raises_on_none_parent():
    with pytest.raises(ValueError):
        add_child_node(None, "x")


def test_add_child_nodes_bulk_and_skip_falsy(simple_root):
    added = add_child_nodes(simple_root, ["a", "", None, "b"])
    assert [c.data for c in added] == ["a", "b"]
    assert children_data_list(simple_root) == ["a", "b"]


# ---------------------------
# add_child_node_at_index / add_child_nodes_from_index
# ---------------------------


def test_add_child_node_at_index_inserts_and_bounds():
    root = create_root_with_children_data_list("R", ["a", "c"])
    # insert at index 1 -> a, b, c
    child = add_child_node_at_index(root, "b", 1)
    assert child is not None
    assert children_data_list(root) == ["a", "b", "c"]
    # invalid index (negative)
    assert add_child_node_at_index(root, "x", -1) is None
    # invalid index (beyond len+1)
    assert add_child_node_at_index(root, "y", 10) is None
    # valid at end (append)
    tail = add_child_node_at_index(root, "z", len(root.children_nodes))
    assert tail is not None
    assert children_data_list(root) == ["a", "b", "c", "z"]


def test_add_child_node_at_index_initializes_children_list_when_none():
    root = create_root("R")
    # simulate children_nodes None
    root.children_nodes = None
    child = add_child_node_at_index(root, "x", 0)
    assert child is not None
    assert children_data_list(root) == ["x"]


def test_add_child_nodes_from_index_inserts_sequence_and_updates_flag():
    root = create_root_with_children_data_list("R", ["a", "d"])
    added = add_child_nodes_from_index(root, ["b", "c"], 1)
    assert [c.data for c in added] == ["b", "c"]
    assert children_data_list(root) == ["a", "b", "c", "d"]
    assert root.is_parent is True


def test_add_child_nodes_from_index_handles_empty_or_out_of_bounds():
    root = create_root_with_children_data_list("R", ["a"])
    assert add_child_nodes_from_index(root, [], 0) is None
    assert add_child_nodes_from_index(root, ["x"], 5) is None
    # index == len is allowed (append)
    added = add_child_nodes_from_index(root, ["b", "c"], 1)
    assert children_data_list(root) == ["a", "b", "c"]


def test_add_child_nodes_from_index_initializes_children_when_none(simple_root):
    simple_root.children_nodes = None
    added = add_child_nodes_from_index(simple_root, ["x", "y"], 0)
    assert [c.data for c in added] == ["x", "y"]
    assert children_data_list(simple_root) == ["x", "y"]


# ---------------------------
# Traversals
# ---------------------------


def test_pre_order_traversal(root_with_nested_tree):
    root = root_with_nested_tree
    out = pre_order_traversal(root, [])
    # A, B, E, F, C, D, G
    assert out == ["A", "B", "E", "F", "C", "D", "G"]


def test_post_order_traversal(root_with_nested_tree):
    root = root_with_nested_tree
    out = post_order_traversal(root, [])
    # E, F, B, C, G, D, A
    assert out == ["E", "F", "B", "C", "G", "D", "A"]


def test_level_order_traversal(root_with_nested_tree):
    root = root_with_nested_tree
    out = level_order_traversal(root, [])
    # A, B, C, D, E, F, G
    assert out == ["A", "B", "C", "D", "E", "F", "G"]


def test_traversals_none_root_returns_none():
    assert pre_order_traversal(None, []) is None
    assert post_order_traversal(None, []) is None
    assert level_order_traversal(None, []) is None


# ---------------------------
# Search (BFS / DFS)
# ---------------------------


def test_bfs_and_dfs_found(root_with_nested_tree):
    root = root_with_nested_tree
    n = breadth_first_search(root, "G")
    assert n is not None and n.data == "G" and n.parent.data == "D"
    m = depth_first_search(root, "E")
    assert m is not None and m.data == "E" and m.parent.data == "B"


def test_bfs_and_dfs_not_found(root_with_nested_tree):
    assert breadth_first_search(root_with_nested_tree, "Z") is None
    assert depth_first_search(root_with_nested_tree, "Z") is None


def test_search_when_children_nodes_is_none(simple_root):
    # simulate a single node with children_nodes=None
    simple_root.children_nodes = None
    # target equals root
    assert breadth_first_search(simple_root, "root") is simple_root
    assert depth_first_search(simple_root, "root") is simple_root
    # non-existing
    assert breadth_first_search(simple_root, "x") is None
    assert depth_first_search(simple_root, "x") is None


# ---------------------------
# Removal
# ---------------------------


def test_search_and_remove_node_reattaches_children(root_with_nested_tree):
    root = root_with_nested_tree
    # Remove B (children E, F) -> they should be reattached to A
    removed = search_and_remove_node(root, "B")
    assert removed is not None
    assert removed.data == "B"
    # Removed node is detached
    assert removed.parent is None
    assert removed.children_nodes == []
    # Root children now: C, D, E, F (order depends on extend after removal)
    # Initial A children: B, C, D
    # After removal B: A children: C, D + (E, F appended)
    assert children_data_list(root) == ["C", "D", "E", "F"]
    # Check parents of E, F updated to A
    e = depth_first_search(root, "E")
    f = depth_first_search(root, "F")
    assert e is not None and e.parent is root
    assert f is not None and f.parent is root


def test_search_and_remove_node_does_not_remove_root(root_with_children_data):
    # Attempt to remove root ("A") should return None
    assert search_and_remove_node(root_with_children_data, "A") is None
    # Tree remains intact
    assert children_data_list(root_with_children_data) == ["B", "C", "D"]


def test_search_and_remove_node_not_found_returns_none(root_with_children_data):
    assert search_and_remove_node(root_with_children_data, "ZZZ") is None


def test_search_and_remove_nodes_multiple(root_with_nested_tree):
    root = root_with_nested_tree
    removed = search_and_remove_nodes(root, ["C", "G", "ZZ"])
    # Should remove C (leaf) and G (leaf under D); "ZZ" ignored
    assert [n.data for n in removed] == ["C", "G"]
    # After removing C and G, root children should be B, D (B has E,F; D becomes leaf)
    # But note earlier tests may have mutated state; use fresh tree in this test!
