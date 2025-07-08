from .singly_linked_list import SinglyLinkedList, SinglyLinkedListNode
from typing import Any


def initialize_sll(sll: SinglyLinkedList, data: Any) -> SinglyLinkedListNode:
    """
    Initialize a singly linked list with the first element.

    Args:
        sll: The singly linked list to initialize
        data: The data for the first node

    Returns:
        The first node of the initialized list

    Raises:
        ValueError: If sll is None
    """
    if sll is None:
        raise ValueError("Singly linked list cannot be None")

    sll.head = SinglyLinkedListNode(data)
    sll.sll_initialized = True
    sll.tail = sll.head
    sll.size = 1

    return sll.head


def insert_sll_element(sll: SinglyLinkedList, element: Any) -> bool:
    """
    Insert an element at the end of the singly linked list.

    Args:
        sll: The singly linked list to insert into
        element: The data to insert

    Returns:
        True if insertion was successful

    Raises:
        ValueError: If sll is None
    """
    if sll is None:
        raise ValueError("Singly linked list cannot be None")

    if not sll.sll_initialized:
        initialize_sll(sll, element)
        return True
    else:
        new_node = SinglyLinkedListNode(element)
        sll.tail.next = new_node
        sll.tail = new_node
        sll.size += 1
        return True


def delete_sll_last_element(sll: SinglyLinkedList) -> SinglyLinkedListNode:
    """
    Delete the last element from the singly linked list.

    Args:
        sll: The singly linked list to delete from

    Returns:
        The deleted node, or None if the list is empty

    Raises:
        ValueError: If sll is None
    """
    if sll is None:
        raise ValueError("Singly linked list cannot be None")

    if not sll.sll_initialized or sll.head is None:
        return None

    # Case 1: Single element in the list
    if sll.size == 1:
        deleted_node = sll.head
        sll.head = None
        sll.tail = None
        sll.size = 0
        sll.sll_initialized = False
        return deleted_node

    # Case 2: Multiple elements - traverse to second-to-last node
    current = sll.head
    while current.next != sll.tail:
        current = current.next

    # Delete the last node
    deleted_node = sll.tail
    current.next = None
    sll.tail = current
    sll.size -= 1

    return deleted_node
