import pytest
from src.data_structures.linked_lists.doubly_linked_list.doubly_linked_list import (
    DoublyLinkedList,
)
from src.data_structures.linked_lists.doubly_linked_list.doubly_linked_list_operations import (
    initialize_dll,
    insert_dll_element,
    insert_dll_nth_element,
    get_element_at_index,
    shallow_clear_dll,
    deep_clear_dll,
    delete_dll_tail_element,
    delete_dll_head_element,
    delete_dll_nth_element,
)


def test_initialize_dll():
    dll = DoublyLinkedList()
    node = initialize_dll(dll, "start")
    assert dll.head == node
    assert dll.tail == node
    assert dll.size == 1

    if node is not None:
        assert node.data == "start"
        assert node.prev is None
        assert node.next is None


def test_insert_dll_element():
    dll = DoublyLinkedList()
    insert_dll_element(dll, "first")
    second = insert_dll_element(dll, "second")
    assert dll.size == 2
    assert dll.tail == second

    if dll.head is not None and second is not None:
        assert dll.head.next == second
        assert second.prev == dll.head


def test_insert_dll_nth_element():
    dll = DoublyLinkedList()
    initialize_dll(dll, "first")
    insert_dll_element(dll, "third")
    second = insert_dll_nth_element(dll, "second", 2)

    assert dll.size == 3

    if dll.head is not None and second is not None and second.next is not None:
        assert dll.head.next == second
        assert second.next.data == "third"


def test_get_element_at_index():
    dll = DoublyLinkedList()
    initialize_dll(dll, "first")
    insert_dll_element(dll, "second")
    node = get_element_at_index(dll, 2)

    if node is not None:
        assert node.data == "second"


def test_shallow_clear_dll():
    dll = DoublyLinkedList()
    initialize_dll(dll, "data")
    shallow_clear_dll(dll)
    assert dll.head is None
    assert dll.tail is None
    assert dll.size == 0
    assert not dll.dll_initialized


def test_deep_clear_dll():
    dll = DoublyLinkedList()
    initialize_dll(dll, "one")
    insert_dll_element(dll, "two")
    deep_clear_dll(dll)
    assert dll.size == 0
    assert not dll.dll_initialized


def test_delete_dll_tail_element():
    dll = DoublyLinkedList()
    initialize_dll(dll, "first")
    insert_dll_element(dll, "second")
    deleted = delete_dll_tail_element(dll)

    if deleted is not None:
        assert deleted.data == "second"

    assert dll.size == 1


def test_delete_dll_head_element():
    dll = DoublyLinkedList()
    initialize_dll(dll, "first")
    insert_dll_element(dll, "second")
    deleted = delete_dll_head_element(dll)

    if deleted is not None:
        assert deleted.data == "first"

    assert dll.size == 1


def test_delete_dll_nth_element():
    dll = DoublyLinkedList()
    initialize_dll(dll, "1")
    insert_dll_element(dll, "2")
    insert_dll_element(dll, "3")
    deleted = delete_dll_nth_element(dll, 2)

    if deleted is not None:
        assert deleted.data == "2"

    assert dll.size == 2
