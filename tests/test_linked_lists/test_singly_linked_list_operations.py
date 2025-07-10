import pytest
from src.data_structures.linked_lists.singly_linked_list.singly_linked_list_operations import (
    SinglyLinkedList,
    SinglyLinkedListNode,
    initialize_sll,
    insert_sll_element,
    insert_sll_first_element,
    insert_sll_nth_element,
    delete_sll_first_element,
    insert_sll_first_element,
    insert_sll_nth_element,
    delete_sll_first_element,
    delete_sll_last_element,
    delete_sll_nth_element,
    delete_sll_multiple_elements,
    insert_sll_multiple_elements,
    get_element_at_index,
    shallow_clear_singly_linked_list,
    deep_clear_singly_linked_list,
)
from src.data_structures.linked_lists.linked_list_utilities import (
    MultipleElementsHandler,
)


class TestInsertOperations:
    def test_initialize_and_insert(self):
        sll = SinglyLinkedList()
        node = initialize_sll(sll, "init")
        assert node.data == "init"
        assert sll.head == node

        node2 = insert_sll_element(sll, "second")
        assert node2.data == "second"
        assert sll.tail == node2

    def test_insert_first_and_nth(self):
        sll = SinglyLinkedList()
        insert_sll_element(sll, "b")
        insert_sll_element(sll, "c")

        node = insert_sll_first_element(sll, "a")
        assert sll.head == node

        insert_sll_nth_element(sll, "middle", 2)
        node = get_element_at_index(2, sll)
        assert node is not None and node.data == "middle"


class TestDeleteOperations:
    def test_delete_first_and_last(self):
        sll = SinglyLinkedList()
        insert_sll_element(sll, "x")
        insert_sll_element(sll, "y")

        deleted_first = delete_sll_first_element(sll)
        assert deleted_first is not None and deleted_first.data == "x"
        deleted_last = delete_sll_last_element(sll)
        assert deleted_last is not None and deleted_last.data == "y"
        assert sll.size == 0

    def test_delete_nth(self):
        sll = SinglyLinkedList()
        for val in ["a", "b", "c", "d"]:
            insert_sll_element(sll, val)

        deleted = delete_sll_nth_element(sll, 3)
        assert deleted is not None
        assert deleted.data == "c"
        assert sll.size == 3
        node = get_element_at_index(3, sll)
        assert node is not None and node.data == "d"


class TestMultipleElementDeletion:
    def test_delete_multiple(self):
        sll = SinglyLinkedList()
        for i in range(1, 6):
            insert_sll_element(sll, f"item{i}")

        indices = [1, 3, 6]

        deleted, skipped = delete_sll_multiple_elements(sll, indices)
        assert len(deleted) == 2
        assert len(skipped) == 1


class TestInsertMultipleElements:
    def test_insert_multiple(self):
        sll = SinglyLinkedList()
        for val in ["start", "between", "almost-end"]:
            insert_sll_element(sll, val)

        handlers = [
            MultipleElementsHandler(index=1, element="start"),
            MultipleElementsHandler(index=2, element="between"),
            MultipleElementsHandler(index=4, element="almost-end"),
            MultipleElementsHandler(index=9, element="out-of-bound"),
        ]

        inserted, skipped = insert_sll_multiple_elements(sll, handlers)

        assert [h.data for h in inserted] == ["start", "between", "almost-end"]
        assert [h.element for h in skipped] == ["out-of-bound"]

        node1 = get_element_at_index(1, sll)
        assert node1 is not None and node1.data == "start"
        node2 = get_element_at_index(2, sll)
        assert node2 is not None and node2.data == "between"
        node3 = get_element_at_index(4, sll)
        assert node3 is not None and node3.data == "almost-end"


class TestGetElementAtIndex:
    def test_valid_index(self):
        sll = SinglyLinkedList()
        node1 = SinglyLinkedListNode("a")
        node2 = SinglyLinkedListNode("b")
        node1.next = node2
        sll.head = node1
        sll.tail = node2
        sll.size = 2
        sll.sll_initialized = True

        result1 = get_element_at_index(1, sll)
        assert result1 is not None
        assert result1.data == "a"

        result2 = get_element_at_index(2, sll)
        assert result2 is not None
        assert result2.data == "b"

    def test_invalid_index_bounds(self):
        sll = SinglyLinkedList()
        sll.head = SinglyLinkedListNode("a")
        sll.size = 1
        sll.sll_initialized = True

        with pytest.raises(IndexError):
            get_element_at_index(0, sll)
        with pytest.raises(IndexError):
            get_element_at_index(2, sll)

    def test_uninitialized_or_none_sll(self):
        assert get_element_at_index(1, SinglyLinkedList()) is None

        sll = SinglyLinkedList()
        sll.sll_initialized = False
        assert get_element_at_index(1, sll) is None


class TestClearFunctions:
    def test_shallow_clear(self):
        sll = SinglyLinkedList()
        sll.head = SinglyLinkedListNode("x")
        sll.tail = sll.head
        sll.size = 1
        sll.sll_initialized = True

        shallow_clear_singly_linked_list(sll)
        assert sll.head is None
        assert sll.tail is None
        assert sll.size == 0
        assert sll.sll_initialized is False

    def test_deep_clear(self):
        sll = SinglyLinkedList()
        node1 = SinglyLinkedListNode("a")
        node2 = SinglyLinkedListNode("b")
        node1.next = node2
        sll.head = node1
        sll.tail = node2
        sll.size = 2
        sll.sll_initialized = True

        deep_clear_singly_linked_list(sll)
        assert sll.head is None
        assert sll.tail is None
        assert sll.size == 0
        assert sll.sll_initialized is False
