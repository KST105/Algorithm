from __future__ import annotations
from typing import Any

class Stack:

    def __init__(self):
        self.__top = None
        self.__count = 0

    class Node:

        def __init__(self, data: Any, prev: Node = None):
            self.data = data
            self.prev = prev

    def push(self, data: Any) -> None:
        node = Stack.Node(data)

        if not self.is_empty():
            node.prev = self.__top

        self.__top = node
        self.__count += 1

    # O(1)

    def pop(self) -> Any:
        if self.is_empty():
            return None

        buff = self.__top.data
        self.__top = self.__top.prev
        self.__count -= 1

        return buff

    # O(1)

    def peek(self) -> Any:
        if self.is_empty():
            return None

        return self.__top.data

    # O(1)

    def is_empty(self) -> bool:
        return self.__count == 0


