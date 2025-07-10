from .singly_linked_list import (
    SinglyLinkedList,
    SinglyLinkedListNode,
    MultipleElementsHandler,
    sort_list_multiple_elements_handlers,
)
from typing import Any, Optional


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
        raise ValueError("Singly linked list cannot be Uninitialized")

    sll.head = SinglyLinkedListNode(data)
    sll.sll_initialized = True
    sll.tail = sll.head
    sll.size = 1

    return sll.head


def insert_sll_element(sll: SinglyLinkedList, element: Any) -> SinglyLinkedListNode:
    """
    Insert an element at the end of the singly linked list.

    Args:
        sll: The singly linked list to insert into
        element: The data to insert

    Returns:
        The inserted node

    Raises:
        ValueError: If sll is None
    """
    if sll is None:
        raise ValueError("Singly linked list cannot be Uninitialized")

    if not sll.sll_initialized:
        return initialize_sll(sll, element)
    else:
        new_node = SinglyLinkedListNode(element)

        if sll.tail is not None:
            sll.tail.next = new_node  # type: ignore

        sll.tail = new_node
        sll.size += 1

        return sll.tail


def delete_sll_last_element(sll: SinglyLinkedList) -> Optional[SinglyLinkedListNode]:
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
        raise ValueError("Singly linked list cannot be Uninitialized")

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

        if current is None:
            break

    # Delete the last node
    deleted_node = sll.tail

    if current is not None:
        current.next = None
        sll.tail = current
        sll.size -= 1

    return deleted_node


def insert_sll_first_element(
    sll: SinglyLinkedList, element: Any
) -> SinglyLinkedListNode:
    if sll is None:
        raise ValueError("Singly linked list cannot be Uninitialized")

    if not sll.sll_initialized:
        return initialize_sll(sll, element)

    new_node = SinglyLinkedListNode(element)
    new_node.next = sll.head  # type: ignore
    sll.head = new_node
    sll.size += 1

    if sll.size == 1:
        sll.tail = new_node
        sll.sll_initialized = True

    return new_node


def insert_sll_multiple_elements(
    sll: SinglyLinkedList, elements_with_indices: list[MultipleElementsHandler]
) -> tuple[list[SinglyLinkedListNode], list[MultipleElementsHandler]]:
    if sll is None or sll.head is None:
        raise ValueError("Singly linked list cannot be Uninitialized")

    results: list[SinglyLinkedListNode] = []
    skipped: list[MultipleElementsHandler] = []

    for handler in sort_list_multiple_elements_handlers(elements_with_indices):
        if handler.index <= 0 or handler.index > sll.size:
            skipped.append(handler)
            continue

        current = sll.head

        if handler.index == 1:
            # If the index is 1, we add the element at the beginning
            node = insert_sll_first_element(sll, handler.element)
            results.append(node)
            continue
        elif handler.index == sll.size:
            # If the index is equal to the size, we add the element at the end
            node = insert_sll_element(sll, handler.element)
            results.append(node)
            continue
        else:  # For other indices, we add the element at the specified position
            if current is None:
                raise ValueError("Singly linked list is empty, cannot add element")

            for _ in range(handler.index - 2):
                if current is None:
                    raise ValueError("Singly linked list cannot be Uninitialized")
                else:
                    current = current.next

            new_node = SinglyLinkedListNode(handler.element)
            new_node.next = current.next if current else None
            current.next = new_node  # type: ignore
            sll.size += 1
            results.append(new_node)

    return (results, skipped)


def insert_sll_nth_element(
    sll: SinglyLinkedList, element: Any, insertion_index: int
) -> SinglyLinkedListNode:
    if sll is None:
        raise ValueError("Singly linked list cannot be Uninitialized")

    if insertion_index <= 0 or insertion_index > sll.size + 1:
        raise IndexError("Insertion index out of bounds")

    if insertion_index == 1:
        return insert_sll_first_element(sll, element)

    if insertion_index == sll.size + 1:
        return insert_sll_element(sll, element)

    current = sll.head

    for _ in range(insertion_index - 2):
        if current is None:
            raise IndexError("Insertion index out of bounds")
        current = current.next

    if current is None:
        raise IndexError("Insertion index out of bounds")

    new_node = SinglyLinkedListNode(element)
    new_node.next = current.next
    current.next = new_node  # type: ignore
    sll.size += 1

    return new_node


def delete_sll_first_element(sll: SinglyLinkedList) -> Optional[SinglyLinkedListNode]:
    if sll is None:
        raise ValueError("Singly linked list cannot be Uninitialized")

    if not sll.sll_initialized or sll.head is None:
        return None

    deleted_node = sll.head
    sll.head = sll.head.next
    sll.size -= 1

    if sll.size == 0:
        sll.tail = None
        sll.sll_initialized = False

    return deleted_node


def delete_sll_nth_element(
    sll: SinglyLinkedList, deletion_index: int
) -> Optional[SinglyLinkedListNode]:
    if sll is None:
        raise ValueError("Singly linked list cannot be Uninitialized")

    if deletion_index <= 0 or deletion_index > sll.size:
        raise IndexError("Deletion index out of bounds")

    if deletion_index == 1:
        return delete_sll_first_element(sll)

    if deletion_index == sll.size:
        return delete_sll_last_element(sll)

    current = sll.head

    for _ in range(deletion_index - 2):
        if current is None:
            raise IndexError("Deletion index out of bounds")

        current = current.next

    if current is None or current.next is None:
        raise IndexError("Deletion index out of bounds")

    deleted_node = current.next
    current.next = deleted_node.next
    sll.size -= 1

    return deleted_node


def delete_sll_multiple_elements(
    sll: SinglyLinkedList, indices: list[int]
) -> tuple[list[MultipleElementsHandler], list[int]]:
    if sll is None or sll.head is None:
        raise ValueError("Singly linked list cannot be Uninitialized")

    results: list[MultipleElementsHandler] = []
    skipped: list[int] = []

    for index in sorted(indices):
        if index <= 0 or index > sll.size:
            skipped.append(index)
            continue

        if index == 1:
            node = delete_sll_first_element(sll)
            results.append(MultipleElementsHandler(index, node.data if node else None))
            continue
        elif index == sll.size:
            node = delete_sll_last_element(sll)
            results.append(MultipleElementsHandler(index, node.data if node else None))
            continue
        else:
            current = sll.head

            for _ in range(index - 2):
                if current is None:
                    raise ValueError("Singly linked list cannot be Uninitialized")

                current = current.next

            if current is None or current.next is None:
                raise ValueError("Singly linked list cannot be Uninitialized")

            deleted_node = current.next
            current.next = deleted_node.next
            sll.size -= 1
            results.append(
                MultipleElementsHandler(
                    index, deleted_node.data if deleted_node else None
                )
            )

    return (results, skipped)


def get_element_at_index(
    index: int, sll: SinglyLinkedList
) -> Optional[SinglyLinkedListNode]:
    if sll is None or not sll.sll_initialized or sll.head is None:
        return None

    if index < 1 or index > sll.size:
        raise IndexError("Index out of bounds")

    current = sll.head
    for _ in range(index - 1):
        if current is None:
            raise IndexError("Index out of bounds")
        current = current.next

    return current


def shallow_clear_singly_linked_list(sll: SinglyLinkedList) -> None:
    """
    Clear the singly linked list, removing all elements.

    Args:
        sll: The singly linked list to clear
    """
    if sll is None:
        raise ValueError("Singly linked list cannot be Uninitialized")

    sll.head = None
    sll.tail = None
    sll.size = 0
    sll.sll_initialized = False


def deep_clear_singly_linked_list(sll: SinglyLinkedList) -> None:
    current = sll.head
    while current:
        next_node = current.next
        current.next = None
        current = next_node

    sll.head = None
    sll.tail = None
    sll.size = 0
    sll.sll_initialized = False


# def sort_sll(sll: SinglyLinkedList) -> SinglyLinkedList:
#     if sll is None or not sll.sll_initialized or sll.head is None:
#         return sll

#     # Extract data from nodes
#     data_list = []
#     current = sll.head
#     while current is not None:
#         data_list.append(current.data)
#         current = current.next

#     # Sort the data
#     sorted_data = sorted(data_list)

#     # Rebuild the linked list with sorted data
#     sll.head = None
#     sll.tail = None
#     sll.size = 0
#     sll.sll_initialized = False

#     for data in sorted_data:
#         insert_sll_element(sll, data)

#     return sll
