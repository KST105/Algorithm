from __future__ import annotations
from typing import Any

# ---------------- LinkedList (Односвязный список) -----------------

# ------- Field (Поля) -------
# 1. count - кол-во элементов списка
# 2. head -

# ------- Interface (Интерфейс) -------
# 1. add_last(data): None  - добавляет элемент data в конец списка
# 2. add_head(data): None  - добавляет элемент data в начало списка
# 3. insert(position, data): None  - вставляет элемент data на позицию position
# 4. get(position): Node | None  - возвращает узел (Node) по позиции. если такой позиции нет, вернуть None
# 5. remove(data): Node  - удаляет первое вхождение элемента data и возвращает его узел
# 6. find(data): Node | None
# 7. count(data): int
# 8. is_empty(): bool


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

    def add_head(self, data: Any) -> None:

        node = Node(data=data, next=None)
        new_node = node(data, self.__head )
        self.__head = new_node
        self.__count += 1

        return None

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

    def is_empty(self) -> bool:
        return self._count == 0
