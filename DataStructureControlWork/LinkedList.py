from __future__ import annotations
from typing import Any

class LinkedList:

    class Node:

        def __init__(self, data: Any, next: Node = None):
            self.data = data
            self.next = next

    def __init__(self):
        self.__count = 0
        self.__head = None

    def add_last(self, data: Any) -> None:

        node = Node(data=data, next=None)

        if self.is_empty():
            self.__head = node
            return

        iterator = self.__head

        while iterator.next is not None:
            iterator = iterator.next

        iterator.next = node

        self.__count += 1

        return None

    # O(n)

    def add_head(self, data: Any) -> None:

        node = Node(data=data, next=None)
        new_node = node(data, self.__head )
        self.__head = new_node
        self.__count += 1

        return None

    # O(1)

    def insert(self, position: int, data: Any) -> None:

        node = Node(data=data, next=None)

        if self.is_empty():
            self.__head = node
            return

        if position > self.__count:
            self.add_last(data)
            return

        iterator = self.__head
        iiterator = 1

        while iiterator <= position-1 and iterator.next is not None:
            iiterator += 1
            iterator = iterator.next

        node.next = iterator.next
        iterator.next = node

        self.__count += 1

    # O(n)

    def get_position(self, position: int) -> Any:

        if not self.__head:
            return None

        if position <= 0:
            return None

        iterator = self.__head
        iiterator = 1

        while iterator is not None:
            if iiterator == position:
                return iterator.data

            iterator = iterator.next
            iiterator += 1

        return None

    # O(n)

    def remove_noda(self, data: Any) -> Any | None:

        if not self.__head:
            return None

        if self.__head.data == data:
            buff = self.__head.data
            self.__head = self.__head.next
            self.__count -= 1

            return buff

        iiterator = self.__head

        while iiterator.next is not None:
            if iiterator.next.data == data:
                buff = iiterator.next.data
                iiterator.next = iiterator.next.next
                self.__count -= 1

                return buff

            iiterator = iiterator.next

        return None

    # O(n)

    def find_data(self, data: Any) -> Any:

        if not self.__head:
            return None

        iterator = self.__head

        iiterator = 1

        while iterator is not None:
            if iterator.data == data:
                return iterator.data, iiterator
            iterator = iterator.next
            iiterator += 1

        return None

    # O(n)

    def count(self, data: Any) -> int:

        if not self.__head:
            return None

        iterator = self.__head
        iiterator = 0

        while iterator is not None:
            if iterator.data == data:
                iiterator += 1
            iterator = iterator.next

        return iiterator

    # O(n)

    def is_empty(self) -> bool:
        return self.__count == 0
