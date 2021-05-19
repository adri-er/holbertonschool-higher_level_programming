#!/usr/bin/python3
""" Creation of classes Node and SinglyLinkedList.

In this module its created the objects inside a linked list (Node class)
and creates a linked list taking into account the previous class, this is done
with methods inside SinglyLinkedLists class.

Example:
   In this example a linked list will be created (s_linked_l_1) and nodes with
   a specific value are added using sorted_insert(value) method.

   s_linked_l_1 = SinglyLinkedList()
   s_linked_l_1.sorted_insert(2)
   s_linked_l_1.sorted_insert(5)
   print(s_linked_l_1)

   The previous code gives the output:
   2
   5
"""


class Node:
    """ Node class with the format of a single linked list is created.

    Attributes:
        data (int): Integer with the value stored in the linked list.
        next_node (Node): Node that corresponds to the next in the linked list.

    """

    def __init__(self, data, next_node=None):
        """ Initialization of the data and next_node arguments in the list.

        Args:
            data (int): integer with the data in the node.
            next_node (Node): Next node in the linked list. It can be None if
               it is the last.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Method to get the value of the data in a Node. """
        return self.__data

    @data.setter
    def data(self, data):
        """Method to set the value of the data in a Node. """
        if type(data) != int:
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def next_node(self):
        """Method to get the value of the next_node in a linked list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        """Method to set the value of the next_node in a linked list."""
        if type(next_node) != Node and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node


class SinglyLinkedList:
    """SinlgyLinkedList class creates a single linked list instance.

    The linked list is organized by the nodes values and each node
    has to be inserted with the method sorted_insert().

    """
    def __init__(self):
        """
        Inititializes the attributes of the single linked list.

        Attributes:
            head (Node): Node that is the head of the singly linked list.

        """
        self.__head = None

    def sorted_insert(self, value):
        """ Inserts a node to the linked list pointed by the head. """
        if self.__head is None:
            new_node = Node(value)
            self.__head = new_node

        elif self.__head.data > value:
            new_node = Node(value, self.__head)
            self.__head = new_node

        else:
            temp = self.__head
            while (temp.next_node is not None):
                if (temp.next_node.data > value):
                    new_node = Node(value, temp.next_node)
                    temp.next_node = new_node
                    return
                temp = temp.next_node
            if (temp.next_node is None):
                new_node = Node(value)
                temp.next_node = new_node

    def __str__(self):
        """Defines the message when a SinglyLinkedList instance is printed."""
        temp = self.__head
        msg = ""
        while temp is not None:
            if temp.next_node is None:
                msg += str(temp.data)
            else:
                msg += str(temp.data) + "\n"
            temp = temp.next_node
        return msg
