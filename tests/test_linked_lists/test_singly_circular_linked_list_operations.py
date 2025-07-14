import pytest
from src.data_structures.linked_lists.singly_circular_linked_list.singly_circular_linked_list import (
    SinglyCircularLinkedList,
)
from src.data_structures.linked_lists.singly_circular_linked_list.singly_circular_linked_list_operations import (
    initialize_sll,
    insert_sll_element,
    insert_sll_first_element,
    insert_sll_nth_element,
    get_element_at_index,
    delete_sll_first_element,
    delete_sll_last_element,
    delete_sll_nth_element,
    shallow_clear_singly_linked_list,
    deep_clear_singly_linked_list,
)


def test_initialize_and_basic_insertions():
    sll = SinglyCircularLinkedList()
    node1 = initialize_sll(sll, "start")
    assert sll.head == node1 and sll.tail == node1
    assert sll.size == 1
    node2 = insert_sll_element(sll, "second")
    assert sll.tail.data == "second"
    node3 = insert_sll_first_element(sll, "first")
    assert sll.head.data == "first"
    assert sll.size == 3


def test_insert_nth_element():
    sll = SinglyCircularLinkedList()
    initialize_sll(sll, "first")
    insert_sll_element(sll, "third")
    node = insert_sll_nth_element(sll, "second", 2)
    assert node.data == "second"
    assert sll.size == 3
    assert get_element_at_index(2, sll).data == "second"


def test_insert_nth_invalid():
    sll = SinglyCircularLinkedList()
    with pytest.raises(ValueError):
        insert_sll_nth_element(sll, "fail", 1)
    initialize_sll(sll, "first")
    with pytest.raises(IndexError):
        insert_sll_nth_element(sll, "fail", 5)


def test_get_element():
    sll = SinglyCircularLinkedList()
    initialize_sll(sll, "one")
    insert_sll_element(sll, "two")
    insert_sll_element(sll, "three")
    assert get_element_at_index(1, sll).data == "one"
    assert get_element_at_index(3, sll).data == "three"
    with pytest.raises(IndexError):
        get_element_at_index(4, sll)


def test_delete_elements():
    sll = SinglyCircularLinkedList()
    initialize_sll(sll, "one")
    insert_sll_element(sll, "two")
    insert_sll_element(sll, "three")
    delete_sll_nth_element(sll, 2)
    assert sll.size == 2
    deleted = delete_sll_last_element(sll)
    assert deleted.data == "three"
    deleted = delete_sll_first_element(sll)
    assert deleted.data == "one"
    assert sll.size == 0


def test_clear_operations():
    sll = SinglyCircularLinkedList()
    initialize_sll(sll, "one")
    insert_sll_element(sll, "two")
    shallow_clear_singly_linked_list(sll)
    assert sll.size == 0 and not sll.sll_initialized
    initialize_sll(sll, "reset")
    insert_sll_element(sll, "again")
    deep_clear_singly_linked_list(sll)
    assert sll.head is None and sll.tail is None and sll.size == 0
