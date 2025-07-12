"""
Operations for doubly linked list manipulation.

This module provides utility functions for performing common operations
on doubly linked lists, including initialization, insertion, deletion, and clearing.
"""

from .doubly_linked_list import (
    DoublyLinkedList,
    DoublyLinkedListNode,
)
from ..linked_list_utilities import (
    MultipleElementsHandler,
    sort_list_multiple_elements_handlers,
)
from typing import Any, Optional


def initialize_dll(dll: DoublyLinkedList, data: Any) -> Optional[DoublyLinkedListNode]:
    """
    Initialize a doubly linked list with the first element.

    This function sets up the list with its first node, establishing both
    head and tail references and marking the list as initialized.

    Args:
        dll (DoublyLinkedList): The doubly linked list to initialize
        data (Any): The data for the first node

    Returns:
        Optional[DoublyLinkedListNode]: The created node, or None if initialization failed

    Example:
        >>> dll = DoublyLinkedList()
        >>> node = initialize_dll(dll, "first")
        >>> print(dll.size)  # Output: 1
    """
    first_node = DoublyLinkedListNode(data)

    dll.head = first_node
    dll.tail = first_node
    dll.size = 1
    dll.dll_initialized = True

    return first_node


def insert_dll_element(
    dll: DoublyLinkedList, data: Any
) -> Optional[DoublyLinkedListNode]:
    """
    Insert an element at the end of the doubly linked list.

    If the list is empty, this function will initialize it with the first element.
    Otherwise, it appends the new element to the end of the list, properly
    maintaining both forward and backward links.

    Args:
        dll (DoublyLinkedList): The doubly linked list to insert into
        data (Any): The data to insert

    Returns:
        Optional[DoublyLinkedListNode]: The created node, or None if insertion failed

    Raises:
        ValueError: If the dll parameter is None

    Example:
        >>> dll = DoublyLinkedList()
        >>> insert_dll_element(dll, "first")
        >>> insert_dll_element(dll, "second")
        >>> print(dll.size)  # Output: 2
    """
    if dll is None:
        raise ValueError("DoublyLinkedList cannot be None")

    new_node = None

    if not dll.dll_initialized:
        new_node = initialize_dll(dll, data)
        return new_node

    if dll.size == 1 and dll.head is not None:
        new_node = DoublyLinkedListNode(data)
        dll.head.next = new_node
        new_node.prev = dll.head
        dll.tail = new_node
        dll.size += 1
    else:
        if dll.tail is not None:
            new_node = DoublyLinkedListNode(data)
            dll.tail.next = new_node
            new_node.prev = dll.tail
            dll.tail = new_node
            dll.size += 1

    return new_node


def insert_dll_nth_element(
    dll: DoublyLinkedList, data: Any, index: int
) -> Optional[DoublyLinkedListNode]:
    """
    Insert an element at the specified index in the doubly linked list.

    This function inserts a new node at the given index position, maintaining
    proper forward and backward links. The index is 1-based.

    Args:
        dll (DoublyLinkedList): The doubly linked list to insert into
        data (Any): The data to insert
        index (int): The index where to insert (1-based indexing)

    Returns:
        Optional[DoublyLinkedListNode]: The created node, or None if insertion failed

    Raises:
        ValueError: If the dll parameter is None or list is not initialized

    Example:
        >>> dll = DoublyLinkedList()
        >>> initialize_dll(dll, "first")
        >>> insert_dll_element(dll, "third")
        >>> insert_dll_nth_element(dll, "second", 2)
        >>> print(dll.size)  # Output: 3
    """
    if dll is None:
        raise ValueError("DoublyLinkedList cannot be None")

    if not dll.dll_initialized:
        raise ValueError(
            "DoublyLinkedList must be initialized before inserting elements"
        )

    new_node = None
    current = dll.head

    for _ in range(index - 2):
        current = current.next if current else None

    if current is not None and current.next is not None:
        new_node = DoublyLinkedListNode(data)

        new_node.next = current.next
        new_node.prev = current
        current.next.prev = new_node
        current.next = new_node
        dll.size += 1

    return new_node


def insert_dll_multiple_elements(
    dll: DoublyLinkedList, elements_with_indices: list[MultipleElementsHandler]
) -> tuple[list[DoublyLinkedListNode], list[int]]:
    """
    Insert multiple elements at specified indices in the doubly linked list.

    This function processes a list of elements with their target indices and
    inserts them into the list. Elements are sorted by index before insertion
    to maintain proper ordering. Invalid indices are skipped.

    Args:
        dll (DoublyLinkedList): The doubly linked list to insert into
        elements_with_indices (list[MultipleElementsHandler]): List of handlers
            containing elements and their target indices

    Returns:
        tuple[list[DoublyLinkedListNode], list[int]]: A tuple containing:
            - List of successfully inserted nodes
            - List of indices that were skipped due to being out of bounds

    Raises:
        ValueError: If the dll parameter is None or list is not initialized

    Example:
        >>> dll = DoublyLinkedList()
        >>> initialize_dll(dll, "base")
        >>> handlers = [
        ...     MultipleElementsHandler(index=1, element="first"),
        ...     MultipleElementsHandler(index=2, element="second")
        ... ]
        >>> inserted, skipped = insert_dll_multiple_elements(dll, handlers)
        >>> print(len(inserted))  # Output: 2
    """
    if dll is None:
        raise ValueError("DoublyLinkedList cannot be None")

    if not dll.dll_initialized:
        raise ValueError(
            "DoublyLinkedList must be initialized before inserting elements"
        )

    sorted_elements_with_indices = sort_list_multiple_elements_handlers(
        elements_with_indices
    )

    inserted = []
    skipped = []
    current = dll.head
    current_index = 1
    first_inserted = False

    for handler in sorted_elements_with_indices:
        if handler.index < 1 or handler.index > dll.size + 1:
            skipped.append(handler.index)
            continue

        new_node = DoublyLinkedListNode(handler.element)

        if not first_inserted:
            for _ in range(handler.index - 1):
                current = current.next if current else None
                current_index += 1

            if current is not None and current.next is not None:
                current.next.prev = new_node
                new_node.next = current.next.prev
                current.next = new_node
                new_node.prev = current

                dll.size += 1
                first_inserted = True
                inserted.append(new_node)

                current = new_node
                current_index += 1
        else:
            for _ in range(handler.index - current_index):
                current = current.next if current else None
                current_index += 1

            if current is not None and current.next is not None:
                current.next.prev = new_node
                new_node.next = current.next.prev
                current.next = new_node
                new_node.prev = current

                dll.size += 1
                first_inserted = True
                inserted.append(new_node)

                current = new_node
                current_index += 1

    return (inserted, skipped)


def get_element_at_index(
    dll: DoublyLinkedList, index: int
) -> Optional[DoublyLinkedListNode]:
    """
    Get the node at the specified index in the doubly linked list.

    This function traverses the list to find and return the node at the
    given index. The index is 1-based.

    Args:
        dll (DoublyLinkedList): The doubly linked list to access
        index (int): The index of the element to retrieve (1-based)

    Returns:
        Optional[DoublyLinkedListNode]: The node at the specified index,
            or None if the index is out of bounds

    Raises:
        ValueError: If the dll parameter is None or list is not initialized

    Example:
        >>> dll = DoublyLinkedList()
        >>> initialize_dll(dll, "first")
        >>> insert_dll_element(dll, "second")
        >>> node = get_element_at_index(dll, 2)
        >>> print(node.data)  # Output: second
    """
    if dll is None:
        raise ValueError("DoublyLinkedList cannot be None")

    if not dll.dll_initialized:
        raise ValueError(
            "DoublyLinkedList must be initialized before accessing elements"
        )

    if index < 1 or index > dll.size:
        return None

    current = dll.head

    for _ in range(index - 1):
        if current is not None:
            current = current.next

    return current


def shallow_clear_dll(dll: DoublyLinkedList):
    """
    Perform a shallow clear of the doubly linked list.

    This function resets the list structure by setting head and tail to None,
    resetting size to 0, and marking the list as uninitialized. It does not
    explicitly break node connections, relying on garbage collection.

    Args:
        dll (DoublyLinkedList): The doubly linked list to clear

    Raises:
        ValueError: If the dll parameter is None

    Example:
        >>> dll = DoublyLinkedList()
        >>> initialize_dll(dll, "data")
        >>> shallow_clear_dll(dll)
        >>> print(dll.size)  # Output: 0
    """
    if dll is None:
        raise ValueError("DoublyLinkedList cannot be None")

    dll.head = None
    dll.tail = None
    dll.size = 0
    dll.dll_initialized = False


def deep_clear_dll(dll: DoublyLinkedList):
    """
    Perform a deep clear of the doubly linked list.

    This function traverses the entire list and explicitly breaks all node
    connections (both forward and backward links) before clearing the list
    structure. This ensures proper cleanup and prevents memory leaks.

    Args:
        dll (DoublyLinkedList): The doubly linked list to clear

    Raises:
        ValueError: If the dll parameter is None

    Example:
        >>> dll = DoublyLinkedList()
        >>> initialize_dll(dll, "data")
        >>> insert_dll_element(dll, "more_data")
        >>> deep_clear_dll(dll)
        >>> print(dll.size)  # Output: 0
    """
    if dll is None:
        raise ValueError("DoublyLinkedList cannot be None")

    current = dll.head
    while current is not None:
        next_node = current.next
        current.prev = None
        current.next = None
        current = next_node

    # Properly reset the list
    dll.head = None
    dll.tail = None
    dll.size = 0
    dll.dll_initialized = False


def delete_dll_tail_element(dll: DoublyLinkedList) -> Optional[DoublyLinkedListNode]:
    """
    Delete the tail (last) element from the doubly linked list.

    This function removes the last node from the list and properly updates
    the tail reference and node connections. If the list becomes empty,
    it is marked as uninitialized.

    Args:
        dll (DoublyLinkedList): The doubly linked list to delete from

    Returns:
        Optional[DoublyLinkedListNode]: The deleted node, or None if deletion failed

    Raises:
        ValueError: If the dll parameter is None, or if the list is not
            initialized or is empty

    Example:
        >>> dll = DoublyLinkedList()
        >>> initialize_dll(dll, "first")
        >>> insert_dll_element(dll, "second")
        >>> deleted = delete_dll_tail_element(dll)
        >>> print(deleted.data)  # Output: second
        >>> print(dll.size)  # Output: 1
    """
    if dll is None:
        raise ValueError("DoublyLinkedList cannot be None")

    if not dll.dll_initialized or dll.size == 0:
        raise ValueError("DoublyLinkedList must be initialized and not empty")

    deleted_node = None

    if dll.size == 1:
        deleted_node = dll.head
        dll.head = None
        dll.tail = None
        dll.size = 0
        dll.dll_initialized = False
    else:
        deleted_node = dll.tail
        if dll.tail is not None and dll.tail.prev is not None:
            new_tail = dll.tail.prev
            new_tail.next = None  # ✅ Add this
            dll.tail.prev = None
            dll.tail = new_tail
            dll.size -= 1  # ✅ Fix this

    return deleted_node


def delete_dll_head_element(dll: DoublyLinkedList) -> Optional[DoublyLinkedListNode]:
    """
    Delete the head (first) element from the doubly linked list.

    This function removes the first node from the list and properly updates
    the head reference and node connections. If the list becomes empty,
    it is marked as uninitialized.

    Args:
        dll (DoublyLinkedList): The doubly linked list to delete from

    Returns:
        Optional[DoublyLinkedListNode]: The deleted node, or None if deletion failed

    Raises:
        ValueError: If the dll parameter is None, or if the list is not
            initialized or is empty

    Example:
        >>> dll = DoublyLinkedList()
        >>> initialize_dll(dll, "first")
        >>> insert_dll_element(dll, "second")
        >>> deleted = delete_dll_head_element(dll)
        >>> print(deleted.data)  # Output: first
        >>> print(dll.size)  # Output: 1
    """
    if dll is None:
        raise ValueError("DoublyLinkedList cannot be None")

    if not dll.dll_initialized or dll.size == 0:
        raise ValueError("DoublyLinkedList must be initialized and not empty")

    if dll.size == 1:
        deleted_node = dll.head
        dll.head = None
        dll.tail = None
        dll.size = 0
        dll.dll_initialized = False
    else:
        deleted_node = dll.head

        if dll.head is not None:
            new_head = dll.head.next

            dll.head.prev = None
            dll.head.next = None
            dll.size -= 1
            dll.head = new_head

    return deleted_node


def delete_dll_nth_element(
    dll: DoublyLinkedList, index: int
) -> Optional[DoublyLinkedListNode]:
    """
    Delete the element at the specified index from the doubly linked list.

    This function removes the node at the given index and properly updates
    the connections between surrounding nodes. The index is 1-based.

    Args:
        dll (DoublyLinkedList): The doubly linked list to delete from
        index (int): The index of the element to delete (1-based)

    Returns:
        Optional[DoublyLinkedListNode]: The deleted node, or None if deletion failed

    Raises:
        ValueError: If the dll parameter is None, or if the list is not
            initialized or is empty
        IndexError: If the index is out of bounds

    Example:
        >>> dll = DoublyLinkedList()
        >>> initialize_dll(dll, "first")
        >>> insert_dll_element(dll, "second")
        >>> insert_dll_element(dll, "third")
        >>> deleted = delete_dll_nth_element(dll, 2)
        >>> print(deleted.data)  # Output: second
        >>> print(dll.size)  # Output: 2
    """
    if dll is None:
        raise ValueError("DoublyLinkedList cannot be None")

    if not dll.dll_initialized or dll.size == 0:
        raise ValueError("DoublyLinkedList must be initialized and not empty")

    if index < 1 or index > dll.size:
        raise IndexError("Index out of bounds")

    deleted_node = None

    if dll.size == 1:
        deleted_node = dll.head
        dll.head = None
        dll.tail = None
        dll.size = 0
        dll.dll_initialized = False
    else:
        current = dll.head

        if dll.head is not None:
            for _ in range(
                index - 1
            ):  # 1 because my linked list's indexing starts from 1
                current = current.next if current else None

        deleted_node = current

        if (
            current is not None
            and current.next is not None
            and current.prev is not None
        ):
            current.prev.next = current.next
            current.next.prev = current.prev
            current.next = None
            current.prev = None
            dll.size -= 1

    return deleted_node


def delete_dll_multiple_elements(
    dll: DoublyLinkedList, elements_with_indices: list[MultipleElementsHandler]
) -> tuple[list[DoublyLinkedListNode], list[int]]:
    """
    Delete multiple elements at specified indices from the doubly linked list.

    This function processes a list of handlers containing indices and deletes
    the corresponding elements from the list. Elements are sorted by index
    before deletion to maintain proper ordering. Invalid indices are skipped.

    Args:
        dll (DoublyLinkedList): The doubly linked list to delete from
        elements_with_indices (list[MultipleElementsHandler]): List of handlers
            containing the indices of elements to delete

    Returns:
        tuple[list[DoublyLinkedListNode], list[int]]: A tuple containing:
            - List of successsfully deleted nodes
            - List of indices that were skipped due to being out of bounds

    Raises:
        ValueError: If the dll parameter is None, or if the list is not
            initialized or is empty

    Example:
        >>> dll = DoublyLinkedList()
        >>> initialize_dll(dll, "first")
        >>> insert_dll_element(dll, "second")
        >>> insert_dll_element(dll, "third")
        >>> handlers = [
        ...     MultipleElementsHandler(index=1, element=""),
        ...     MultipleElementsHandler(index=3, element="")
        ... ]
        >>> deleted, skipped = delete_dll_multiple_elements(dll, handlers)
        >>> print(len(deleted))  # Output: 2
        >>> print(dll.size)  # Output: 1
    """
    if dll is None:
        raise ValueError("DoublyLinkedList cannot be None")

    if not dll.dll_initialized or dll.size == 0:
        raise ValueError("DoublyLinkedList must be initialized and not empty")

    sorted_elements_with_indices = sort_list_multiple_elements_handlers(
        elements_with_indices
    )

    deleted: list[DoublyLinkedListNode] = []
    skipped: list[int] = []
    current = dll.head
    current_index = 1
    first_deleted = False

    for handler in sorted_elements_with_indices:
        if handler.index < 1 or handler.index > dll.size:
            skipped.append(handler.index)
            continue

        if not first_deleted:
            for _ in range(handler.index - 1):
                current = current.next if current is not None else None
                current_index += 1

            deleted_node = current
            if (
                deleted_node is not None
                and deleted_node.prev is not None
                and deleted_node.next is not None
            ):
                deleted_node.prev.next = deleted_node.next
                deleted_node.next.prev = deleted_node.prev
                deleted_node.next = None
                deleted_node.prev = None
                dll.size -= 1
                deleted.append(deleted_node)
                first_deleted = True
        else:
            for _ in range(handler.index - current_index):
                current = current.next if current is not None else None
                current_index += 1

            deleted_node = current
            if (
                deleted_node is not None
                and deleted_node.prev is not None
                and deleted_node.next is not None
            ):
                deleted_node.prev.next = deleted_node.next
                deleted_node.next.prev = deleted_node.prev
                deleted_node.next = None
                deleted_node.prev = None
                dll.size -= 1
                deleted.append(deleted_node)

    return (deleted, skipped)
