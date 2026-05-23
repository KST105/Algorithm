from __future__ import annotations
from typing import Any

class  Queue:

    class Node:

        def __init__(self,  data: Any, prev: Node = None):

            self.data = data
            self.prev = prev

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def enqueue(self, data: Any) -> None:

        node = self.Node(data)

        if self.is_empty():
            self.__head = node
            self.__tail = node

        else:
            self.__tail.prev = node
            self.__tail = node

        self.__count += 1

    # O(1)

    def dequeue(self) -> Any:

        if self.is_empty():
            return None

        removed = self.__head.data

        if self.__head == self.__tail:
            self.__head = None
            self.__tail = None

        else:
            self.__head = self.__head.prev

        self.__count -= 1

        return removed

    # O(1)

    def peek(self) -> Any:

        if self.is_empty():
            return None

        return self.__head.data

    # O(1)

    def count(self) -> int:
        return self.__count

    # O(1)

    def is_empty(self) -> bool:
        return self.__count == 0

    # O(1)

