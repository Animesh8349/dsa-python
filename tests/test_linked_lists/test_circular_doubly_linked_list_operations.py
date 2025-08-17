import pytest
from src.data_structures.linked_lists.circular_doubly_linked_list.circular_doubly_linked_list import (
    CircularDoublyLinkedListNode,
    CircularDoublyLinkedList,
)
from src.data_structures.linked_lists.circular_doubly_linked_list.circular_doubly_linked_list_operations import (
    initialize_cdll,
    insert_cdll_element,
    insert_cdll_first_element,
    insert_cdll_nth_element,
    get_element_at_index,
    delete_cdll_first_element,
    delete_cdll_last_element,
    delete_cdll_nth_element,
    shallow_clear_doubly_linked_list,
    deep_clear_doubly_linked_list,
)


def test_initialize_and_insertions():
    cdll = CircularDoublyLinkedList()
    node = initialize_cdll(cdll, "start")
    assert cdll.head == node and cdll.tail == node
    assert cdll.size == 1
    assert (
        cdll.head is not None
        and cdll.head.next == cdll.head
        and isinstance(cdll.head.prev, CircularDoublyLinkedListNode)
    )


def test_insert_at_end_and_start():
    cdll = CircularDoublyLinkedList()
    initialize_cdll(cdll, "mid")
    insert_cdll_element(cdll, "end")
    insert_cdll_first_element(cdll, "start")
    assert cdll.size == 3
    assert cdll.head is not None and cdll.head.data == "start"
    assert cdll.tail is not None and cdll.tail.data == "end"


def test_insert_nth_and_get_element():
    cdll = CircularDoublyLinkedList()
    initialize_cdll(cdll, "first")
    insert_cdll_element(cdll, "third")
    insert_cdll_nth_element(cdll, "second", 2)
    elem = get_element_at_index(2, cdll)
    assert elem is not None and elem.data == "second"


def test_invalid_insertions():
    cdll = CircularDoublyLinkedList()
    with pytest.raises(ValueError):
        insert_cdll_nth_element(cdll, "fail", 1)
    initialize_cdll(cdll, "only")
    with pytest.raises(IndexError):
        insert_cdll_nth_element(cdll, "out", 5)


def test_deletions():
    cdll = CircularDoublyLinkedList()
    initialize_cdll(cdll, "one")
    insert_cdll_element(cdll, "two")
    insert_cdll_element(cdll, "three")
    deleted = delete_cdll_nth_element(cdll, 2)
    assert deleted is not None and deleted.data == "two"
    deleted = delete_cdll_last_element(cdll)
    assert deleted is not None and deleted.data == "three"
    deleted = delete_cdll_first_element(cdll)
    assert deleted is not None and deleted.data == "one"
    assert cdll.size == 0


def test_invalid_deletions():
    cdll = CircularDoublyLinkedList()
    with pytest.raises(ValueError):
        delete_cdll_nth_element(cdll, 1)
    initialize_cdll(cdll, "x")
    with pytest.raises(IndexError):
        delete_cdll_nth_element(cdll, 2)


def test_clear_behaviors():
    cdll = CircularDoublyLinkedList()
    initialize_cdll(cdll, "one")
    insert_cdll_element(cdll, "two")
    shallow_clear_doubly_linked_list(cdll)
    assert cdll.size == 0 and not cdll.cdll_initialized

    initialize_cdll(cdll, "three")
    insert_cdll_element(cdll, "four")
    deep_clear_doubly_linked_list(cdll)
    assert cdll.head is None and cdll.tail is None and cdll.size == 0
