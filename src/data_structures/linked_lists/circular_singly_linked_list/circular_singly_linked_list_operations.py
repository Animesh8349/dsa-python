from .circular_singly_linked_list import (
    CircularSinglyLinkedList,
    CircularSinglyLinkedListNode,
)
from ..linked_list_utilities import (
    MultipleElementsHandler,
    sort_list_multiple_elements_handlers,
)

from typing import Any, Optional


def initialize_csll(
    csll: CircularSinglyLinkedList, data: Any
) -> CircularSinglyLinkedListNode:
    """
    Initialize a singly circular linked list with the first element.

    Args:
        csll: The singly circular linked list to initialize
        data: The data for the first node

    Returns:
        The first node of the initialized list

    Raises:
        ValueError: If csll is None
    """
    if csll is None:
        raise ValueError("Singly circular linked list cannot be Uninitialized")

    csll.head = CircularSinglyLinkedListNode(data)
    csll.csll_initialized = True
    csll.tail = csll.head
    csll.size = 1

    return csll.head


def insert_csll_element(
    csll: CircularSinglyLinkedList, element: Any
) -> CircularSinglyLinkedListNode:
    """
    Insert an element at the end of the singly circular linked list.

    Args:
        csll: The singly circular linked list to insert into
        element: The data to insert

    Returns:
        The inserted node

    Raises:
        ValueError: If csll is None
    """
    if csll is None:
        raise ValueError("Singly circular linked list cannot be Uninitialized")

    if not csll.csll_initialized:
        return initialize_csll(csll, element)
    else:
        new_node = CircularSinglyLinkedListNode(element)

        if csll.tail is not None:
            csll.tail.next = new_node
            new_node.next = csll.head

        csll.tail = new_node
        csll.size += 1

        return csll.tail


def insert_csll_first_element(
    csll: CircularSinglyLinkedList, element: Any
) -> CircularSinglyLinkedListNode:
    if csll is None:
        raise ValueError("Singly circular linked list cannot be Uninitialized")

    if not csll.csll_initialized:
        return initialize_csll(csll, element)

    new_node = CircularSinglyLinkedListNode(element)

    new_node.next = csll.head
    csll.head = new_node
    csll.tail.next = new_node
    csll.size += 1

    return new_node


def insert_csll_nth_element(
    csll: CircularSinglyLinkedList, element: Any, insertion_index: int
) -> CircularSinglyLinkedListNode:
    if csll is None:
        raise ValueError("Singly circular linked list cannot be Uninitialized")

    if insertion_index <= 0 or insertion_index > csll.size + 1:
        raise IndexError("Insertion index out of bounds")

    if insertion_index == 1:
        return insert_csll_first_element(csll, element)

    if insertion_index == csll.size + 1:
        return insert_csll_element(csll, element)

    current = csll.head

    for _ in range(insertion_index - 2):
        if current is None:
            raise IndexError("Insertion index out of bounds")
        current = current.next

    if current is None:
        raise IndexError("Insertion index out of bounds")

    new_node = CircularSinglyLinkedListNode(element)
    new_node.next = current.next
    current.next = new_node  # type: ignore
    csll.size += 1

    return new_node


def insert_csll_multiple_elements(
    csll: CircularSinglyLinkedList, elements_with_indices: list[MultipleElementsHandler]
) -> tuple[list[CircularSinglyLinkedListNode], list[MultipleElementsHandler]]:
    if csll is None or csll.head is None:
        raise ValueError("Singly circular linked list cannot be Uninitialized")

    results: list[CircularSinglyLinkedListNode] = []
    skipped: list[MultipleElementsHandler] = []

    for handler in sort_list_multiple_elements_handlers(elements_with_indices):
        if handler.index <= 0 or handler.index > csll.size:
            skipped.append(handler)
            continue

        current = csll.head

        if handler.index == 1:
            # If the index is 1, we add the element at the beginning
            node = insert_csll_first_element(csll, handler.element)
            results.append(node)
            continue
        elif handler.index == csll.size:
            # If the index is equal to the size, we add the element at the end
            node = insert_csll_element(csll, handler.element)
            results.append(node)
            continue
        else:  # For other indices, we add the element at the specified position
            if current is None:
                raise ValueError(
                    "Singly circular linked list is empty, cannot add element"
                )

            for _ in range(handler.index - 2):
                if current is None:
                    raise ValueError(
                        "Singly circular linked list cannot be Uninitialized"
                    )
                else:
                    current = current.next

            new_node = CircularSinglyLinkedListNode(handler.element)
            new_node.next = current.next if current else None
            current.next = new_node  # type: ignore
            csll.size += 1
            results.append(new_node)

    return (results, skipped)


def delete_csll_first_element(
    csll: CircularSinglyLinkedList,
) -> Optional[CircularSinglyLinkedListNode]:
    if csll is None:
        raise ValueError("Singly circular linked list cannot be Uninitialized")

    if not csll.csll_initialized or csll.head is None:
        return None

    deleted_node = csll.head
    csll.head = csll.head.next
    csll.size -= 1

    if csll.size == 1:
        csll.tail.next = None
    elif csll.size == 0:
        csll.tail = None
        csll.csll_initialized = False

    return deleted_node


def delete_csll_last_element(
    csll: CircularSinglyLinkedList,
) -> Optional[CircularSinglyLinkedListNode]:
    """
    Delete the last element from the singly circular linked list.

    Args:
        csll: The singly circular linked list to delete from

    Returns:
        The deleted node, or None if the list is empty

    Raises:
        ValueError: If csll is None
    """
    if csll is None:
        raise ValueError("Singly circular linked list cannot be Uninitialized")

    if not csll.csll_initialized or csll.head is None:
        return None

    # Case 1: Single element in the list
    if csll.size == 1:
        deleted_node = csll.head
        csll.head = None
        csll.tail = None
        csll.size = 0
        csll.csll_initialized = False

        return deleted_node

    # Case 2: Multiple elements - traverse to second-to-last node
    current = csll.head

    while current.next != csll.tail:
        current = current.next

        if current is None:
            break

    # Delete the last node
    deleted_node = csll.tail

    if current is not None:
        current.next = deleted_node.next
        csll.tail = current
        csll.size -= 1

    if csll.size == 1:
        csll.tail.next = None

    return deleted_node


def delete_csll_nth_element(
    csll: CircularSinglyLinkedList, deletion_index: int
) -> Optional[CircularSinglyLinkedListNode]:
    if csll is None:
        raise ValueError("Singly circular linked list cannot be Uninitialized")

    if deletion_index <= 0 or deletion_index > csll.size:
        raise IndexError("Deletion index out of bounds")

    if deletion_index == 1:
        return delete_csll_first_element(csll)

    if deletion_index == csll.size:
        return delete_csll_last_element(csll)

    current = csll.head

    for _ in range(deletion_index - 2):
        if current is None:
            raise IndexError("Deletion index out of bounds")

        current = current.next

    if current is None or current.next is None:
        raise IndexError("Deletion index out of bounds")

    deleted_node = current.next
    current.next = deleted_node.next
    csll.size -= 1

    return deleted_node


def delete_csll_multiple_elements(
    csll: CircularSinglyLinkedList, indices: list[int]
) -> tuple[list[MultipleElementsHandler], list[int]]:
    if csll is None or csll.head is None:
        raise ValueError("Singly circular linked list cannot be Uninitialized")

    results: list[MultipleElementsHandler] = []
    skipped: list[int] = []

    for index in sorted(indices):
        if index <= 0 or index > csll.size:
            skipped.append(index)
            continue

        if index == 1:
            node = delete_csll_first_element(csll)
            results.append(MultipleElementsHandler(index, node.data if node else None))
            continue
        elif index == csll.size:
            node = delete_csll_last_element(csll)
            results.append(MultipleElementsHandler(index, node.data if node else None))
            continue
        else:
            current = csll.head

            for _ in range(index - 2):
                if current is None:
                    raise ValueError(
                        "Singly circular linked list cannot be Uninitialized"
                    )

                current = current.next

            if current is None or current.next is None:
                raise ValueError("Singly circular linked list cannot be Uninitialized")

            deleted_node = current.next
            current.next = deleted_node.next
            csll.size -= 1
            results.append(
                MultipleElementsHandler(
                    index, deleted_node.data if deleted_node else None
                )
            )

    return (results, skipped)


def get_element_at_index(
    index: int, csll: CircularSinglyLinkedList
) -> Optional[CircularSinglyLinkedListNode]:
    if csll is None or not csll.csll_initialized or csll.head is None:
        return None

    if index < 1 or index > csll.size:
        raise IndexError("Index out of bounds")

    current = csll.head
    for _ in range(index - 1):
        if current is None:
            raise IndexError("Index out of bounds")
        current = current.next

    return current


def shallow_clear_singly_linked_list(csll: CircularSinglyLinkedList) -> None:
    """
    Clear the singly circular linked list, removing all elements.

    Args:
        csll: The singly circular linked list to clear
    """
    if csll is None:
        raise ValueError("Singly circular linked list cannot be Uninitialized")

    csll.head = None
    csll.tail.next = None
    csll.tail = None
    csll.size = 0
    csll.csll_initialized = False


def deep_clear_singly_linked_list(csll: CircularSinglyLinkedList) -> None:
    if csll is None or not csll.csll_initialized or csll.head is None:
        return

    current = csll.head

    while current:
        next_node = current.next
        current.next = None
        current = next_node
        csll.size -= 1

        if csll.size == 1:
            csll.tail.next = None
        else:
            csll.tail.next = current

    csll.head = None
    csll.tail = None
    csll.size = 0
    csll.csll_initialized = False
