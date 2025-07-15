from .circular_doubly_linked_list import (
    CircularDoublyLinkedList,
    CircularDoublyLinkedListNode,
)
from ..linked_list_utilities import (
    MultipleElementsHandler,
    sort_list_multiple_elements_handlers,
)

from typing import Any, Optional


def initialize_cdll(
    cdll: CircularDoublyLinkedList, data: Any
) -> CircularDoublyLinkedListNode:
    """
    Initialize a doubly circular linked list with the first element.

    Args:
        cdll: The doubly circular linked list to initialize
        data: The data for the first node

    Returns:
        The first node of the initialized list

    Raises:
        ValueError: If cdll is None
    """
    if cdll is None:
        raise ValueError("Doubly circular linked list cannot be Uninitialized")

    cdll.head = CircularDoublyLinkedListNode(data)
    cdll.cdll_initialized = True
    cdll.tail = cdll.head
    cdll.size = 1

    return cdll.head


def insert_cdll_element(
    cdll: CircularDoublyLinkedList, element: Any
) -> CircularDoublyLinkedListNode:
    """
    Insert an element at the end of the doubly circular linked list.

    Args:
        cdll: The doubly circular linked list to insert into
        element: The data to insert

    Returns:
        The inserted node

    Raises:
        ValueError: If cdll is None
    """
    if cdll is None:
        raise ValueError("Doubly circular linked list cannot be Uninitialized")

    if not cdll.cdll_initialized:
        return initialize_cdll(cdll, element)
    else:
        new_node = CircularDoublyLinkedListNode(element)

        if cdll.tail is not None:
            cdll.tail.next = new_node
        elif cdll.head is not None:
            cdll.head.next = new_node

        new_node.prev = cdll.tail
        new_node.next = cdll.head

        if cdll.head is not None:
            cdll.head.prev = new_node

        cdll.tail = new_node
        cdll.size += 1

        return cdll.tail


def insert_cdll_first_element(
    cdll: CircularDoublyLinkedList, element: Any
) -> CircularDoublyLinkedListNode:
    if cdll is None:
        raise ValueError("Doubly circular linked list cannot be Uninitialized")

    if not cdll.cdll_initialized:
        return initialize_cdll(cdll, element)

    new_node = CircularDoublyLinkedListNode(element)

    if new_node is not None and cdll.head is not None and cdll.tail is not None:
        new_node.next = cdll.head
        cdll.head.prev = new_node
        cdll.head = new_node
        cdll.tail.next = new_node
        new_node.prev = cdll.tail
        cdll.size += 1

    return new_node


def insert_cdll_nth_element(
    cdll: CircularDoublyLinkedList, element: Any, insertion_index: int
) -> CircularDoublyLinkedListNode:
    if cdll is None:
        raise ValueError("Doubly circular linked list cannot be Uninitialized")

    if insertion_index <= 0 or insertion_index > cdll.size + 1:
        raise IndexError("Insertion index out of bounds")

    if insertion_index == 1:
        return insert_cdll_first_element(cdll, element)

    if insertion_index == cdll.size + 1:
        return insert_cdll_element(cdll, element)

    current = cdll.head

    for _ in range(insertion_index - 2):
        if current is None:
            raise IndexError("Insertion index out of bounds")
        current = current.next

    if current is None:
        raise IndexError("Insertion index out of bounds")

    new_node = CircularDoublyLinkedListNode(element)
    new_node.next = current.next
    current.next = new_node  # type: ignore
    cdll.size += 1

    return new_node


def insert_cdll_multiple_elements(
    cdll: CircularDoublyLinkedList, elements_with_indices: list[MultipleElementsHandler]
) -> tuple[list[CircularDoublyLinkedListNode], list[MultipleElementsHandler]]:
    if cdll is None or cdll.head is None:
        raise ValueError("Doubly circular linked list cannot be Uninitialized")

    results: list[CircularDoublyLinkedListNode] = []
    skipped: list[MultipleElementsHandler] = []

    for handler in sort_list_multiple_elements_handlers(elements_with_indices):
        if handler.index <= 0 or handler.index > cdll.size:
            skipped.append(handler)
            continue

        current = cdll.head

        if handler.index == 1:
            # If the index is 1, we add the element at the beginning
            node = insert_cdll_first_element(cdll, handler.element)
            results.append(node)
            continue
        elif handler.index == cdll.size:
            # If the index is equal to the size, we add the element at the end
            node = insert_cdll_element(cdll, handler.element)
            results.append(node)
            continue
        else:  # For other indices, we add the element at the specified position
            if current is None:
                raise ValueError(
                    "Doubly circular linked list is empty, cannot add element"
                )

            for _ in range(handler.index - 2):
                if current is None:
                    raise ValueError(
                        "Doubly circular linked list cannot be Uninitialized"
                    )
                else:
                    current = current.next

            new_node = CircularDoublyLinkedListNode(handler.element)
            new_node.next = current.next if current else None
            current.next = new_node  # type: ignore
            cdll.size += 1
            results.append(new_node)

    return (results, skipped)


def delete_cdll_first_element(
    cdll: CircularDoublyLinkedList,
) -> Optional[CircularDoublyLinkedListNode]:
    if cdll is None:
        raise ValueError("Doubly circular linked list cannot be Uninitialized")

    if not cdll.cdll_initialized or cdll.head is None:
        return None

    deleted_node = cdll.head

    # Case 1: Single element in the list
    if cdll.size == 1:
        cdll.head = None
        cdll.tail = None
        cdll.size = 0
        cdll.cdll_initialized = False

        return deleted_node

    if cdll.head is not None and cdll.head.next is not None and cdll.tail is not None:
        cdll.head.next.prev = cdll.head.prev
        cdll.tail.next = cdll.head.next
        cdll.head = cdll.head.next
        cdll.size -= 1

        if cdll.size == 1:
            cdll.tail.next = None
            cdll.head.prev = None
        elif cdll.size == 0:
            cdll.head = None
            cdll.tail = None
            cdll.cdll_initialized = False

    return deleted_node


def delete_cdll_last_element(
    cdll: CircularDoublyLinkedList,
) -> Optional[CircularDoublyLinkedListNode]:
    """
    Delete the last element from the doubly circular linked list.

    Args:
        cdll: The doubly circular linked list to delete from

    Returns:
        The deleted node, or None if the list is empty

    Raises:
        ValueError: If cdll is None
    """
    if cdll is None:
        raise ValueError("Doubly circular linked list cannot be Uninitialized")

    if not cdll.cdll_initialized or cdll.head is None:
        return None

    # Single element in the list
    if cdll.size == 1:
        deleted_node = cdll.head
        cdll.head = None
        cdll.tail = None
        cdll.size = 0
        cdll.cdll_initialized = False

        return deleted_node

    # Delete the last node
    deleted_node = cdll.tail

    if (
        deleted_node is not None
        and deleted_node.next is not None
        and deleted_node.prev is not None
    ):
        deleted_node.next.prev = deleted_node.prev
        deleted_node.prev.next = deleted_node.next

    cdll.size -= 1

    if cdll.size == 1:
        cdll.head.next = None
        cdll.head.prev = None

    return deleted_node


def delete_cdll_nth_element(
    cdll: CircularDoublyLinkedList, deletion_index: int
) -> Optional[CircularDoublyLinkedListNode]:
    if cdll is None:
        raise ValueError("Doubly circular linked list cannot be Uninitialized")

    if deletion_index <= 0 or deletion_index > cdll.size:
        raise IndexError("Deletion index out of bounds")

    if deletion_index == 1:
        return delete_cdll_first_element(cdll)

    if deletion_index == cdll.size:
        return delete_cdll_last_element(cdll)

    current = cdll.head

    for _ in range(deletion_index - 2):
        if current is None:
            raise IndexError("Deletion index out of bounds")

        current = current.next

    if current is None or current.next is None:
        raise IndexError("Deletion index out of bounds")

    deleted_node = current.next
    current.next = deleted_node.next
    cdll.size -= 1

    return deleted_node


def delete_cdll_multiple_elements(
    cdll: CircularDoublyLinkedList, indices: list[int]
) -> tuple[list[MultipleElementsHandler], list[int]]:
    if cdll is None or cdll.head is None:
        raise ValueError("Doubly circular linked list cannot be Uninitialized")

    results: list[MultipleElementsHandler] = []
    skipped: list[int] = []

    for index in sorted(indices):
        if index <= 0 or index > cdll.size:
            skipped.append(index)
            continue

        if index == 1:
            node = delete_cdll_first_element(cdll)
            results.append(MultipleElementsHandler(index, node.data if node else None))
            continue
        elif index == cdll.size:
            node = delete_cdll_last_element(cdll)
            results.append(MultipleElementsHandler(index, node.data if node else None))
            continue
        else:
            current = cdll.head

            for _ in range(index - 2):
                if current is None:
                    raise ValueError(
                        "Doubly circular linked list cannot be Uninitialized"
                    )

                current = current.next

            if current is None or current.next is None:
                raise ValueError("Doubly circular linked list cannot be Uninitialized")

            deleted_node = current.next
            current.next = deleted_node.next
            cdll.size -= 1
            results.append(
                MultipleElementsHandler(
                    index, deleted_node.data if deleted_node else None
                )
            )

    return (results, skipped)


def get_element_at_index(
    index: int, cdll: CircularDoublyLinkedList
) -> Optional[CircularDoublyLinkedListNode]:
    if cdll is None or not cdll.cdll_initialized or cdll.head is None:
        return None

    if index < 1 or index > cdll.size:
        raise IndexError("Index out of bounds")

    current = cdll.head
    for _ in range(index - 1):
        if current is None:
            raise IndexError("Index out of bounds")
        current = current.next

    return current


def shallow_clear_doubly_linked_list(cdll: CircularDoublyLinkedList) -> None:
    """
    Clear the doubly circular linked list, removing all elements.

    Args:
        cdll: The doubly circular linked list to clear
    """
    if cdll is None:
        raise ValueError("Doubly circular linked list cannot be Uninitialized")

    cdll.head = None

    if cdll.tail is not None:
        cdll.tail.next = None

    cdll.tail = None
    cdll.size = 0
    cdll.cdll_initialized = False


def deep_clear_doubly_linked_list(cdll: CircularDoublyLinkedList) -> None:
    if cdll is None or not cdll.cdll_initialized or cdll.head is None:
        return

    current = cdll.head

    while current:
        next_node = current.next
        current.next = None
        current = next_node
        cdll.size -= 1

        if cdll.size == 1 and cdll.tail is not None:
            cdll.tail.next = None
        elif cdll.tail is not None:
            cdll.tail.next = current

    cdll.head = None
    cdll.tail = None
    cdll.size = 0
    cdll.cdll_initialized = False
