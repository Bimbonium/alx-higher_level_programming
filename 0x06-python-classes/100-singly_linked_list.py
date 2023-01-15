#!/usr/bin/python3
"""Class to define singly linked list using python"""


class Node:
    """Node definition"""
    def __init__(self, data, next_node=None):
        """Define Init method"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for data"""
        if(not isinstance(value, int)):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter for next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for next node"""
        if(not isinstance(value, Node) and value is not None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """singly linked list definition"""
    __head = None

    def __init__(self):
        """initializing list"""
        pass

    def __str__(self):
        """define str method for printing"""
        newList = []
        while(self.__head):
            newList.append(self.__head.data)
            self.__head = self.__head.next_node
        return("\n".join([str(x) for x in sorted(newList)]))

    def sorted_insert(self, value):
        """Sorted insert"""
        newNode = Node(value, self.__head)
        self.__head = newNode
