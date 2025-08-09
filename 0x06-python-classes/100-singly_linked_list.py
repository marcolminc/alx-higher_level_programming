#!/usr/bin/python3

"""A module that defines a singly linked list implementation.

This module contains two classes:
- Node: Represents a node in the linked list
- SinglyLinkedList: Manages the linked list with sorted insertion.
"""


class Node:
    """A node in a singly linked list.

    Attributes:
        data (int): The data stored in the node.
        next_node (Node): Reference to the next node in the list.
    """

    def __init__(self, data, next_node=None):
        """Initialize a new Node instance.

        Args:
            data (int): The data to store in the node
            next_node (Node, optional): the next node in the list. Must be a
            Node. Defaults to None.

        Raises:
        TypeError: If data is not an integer or next_node is not a Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """int: Get or set the node's data, with validation.

        Raises:
            TypeError: If data is not an integer
        """
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Node: Get or set the next node reference.

        Raises:
            TypeError: If next_node is not a Node object.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """A singly linked list implementation with sorted insertion.

    Attributes:
        __head (Node): The first node in the linked list
    """

    def __init__(self):
        """Initialize an empty linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new node into the correct sorted position.

        Args:
            value (int): data (value) to insert

        Raises:
            TypeError: if value is not an integer
        """
        if not isinstance(value, int):
            raise TypeError('value must be an integer')
        new = Node(value)
        if self.__head is None:
            self.__head = new
        else:
            curr = self.__head
            nxt = curr.next_node
            while curr:
                if curr.data > value:
                    self.__head = new
                    new.next_node = curr
                    return
                if not nxt:
                    curr.next_node = new
                    return
                if curr.data < value <= nxt.data:
                    curr.next_node = new
                    new.next_node = nxt
                    return
                curr = nxt
                nxt = nxt.next_node

    def __str__(self):
        """Return a string representation of the linked list.

        Returns:
            str: Each node's data on a separate line
        """
        nodes = []
        current = self.__head
        while current:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)
