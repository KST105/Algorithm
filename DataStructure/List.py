from typing import Any

class List:

    @staticmethod
    def __malloc(type, number):
        return [None]*number

    @staticmethod
    def __realloc(memory, type, old_size, new_size):
        new_memory = List.__malloc(int, new_size)

        for i in range(0, old_size, 1):
            new_memory[i] = memory[i]

        return new_memory

    def __init__(self):
        self.__count = 0
        self.__size = 4
        self.__memory = List.__malloc(int, self.__size)

    def __str__(self):
        return str(self.__memory)

    def add(self, data: Any):
        if self.__count == self.__size:
            new_size = self.__size + (self.__size // 2)

            self.__memory = List.__realloc(self.__memory, int, self.__size, new_size)
            self.__size = new_size

        self.__memory[self.__count] = data
        self.__count += 1

        # O(1), O(1), O(1)

    def add_head(self, data: Any):

        if self.__count == self.__size:
            new_size = self.__size + (self.__size // 2)

            self.__memory = List.__realloc(self.__memory, int, self.__size, new_size)
            self.__size = new_size

        for i in range(self.__count, 0, -1):
            self.__memory[i] = self.__memory[i - 1]

        self.__memory[0] = data
        self.__count += 1

        # O(1), O(n), O(n)

    def insert(self, index: int, data: Any):

        if self.__count == self.__size:
            new_size = self.__size + (self.__size // 2)

            self.__memory = List.__realloc(self.__memory, int, self.__size, new_size)
            self.__size = new_size

        for i in range(self.__count, index, -1):
            self.__memory[i] = self.__memory[i - 1]

        self.__memory[index] = data
        self.__count += 1

        # O(1), O(n), O(n)


    def remove(self, data: Any):

        if self.__count == 0:
            return None

        if self.__count == 1 and self.__memory[0] == data:
            self.__memory[0] = None
            self.__count -= 1

        target_index = -1

        for i in range(self.__count):
            if self.__memory[i] == data:
                target_index = i
                break

        if target_index == -1:
            return

        for i in range(target_index, self.__count - 1):
            self.__memory[i] = self.__memory[i + 1]

        self.__count -= 1
        self.__memory[self.__count] = None

    # O(1), O(n), O(n)


    def pop(self, index: int):

        if index >= self.__count or index < 0:
            return None

        for i in range(index, self.__count-1 , 1):
            self.__memory[i] = self.__memory[i + 1]

        self.__count -= 1

    # O(n), O(n), O(n)

    def count(self, item: Any) -> int:

        counter = 0

        for i in range(0, self.__count, 1):
            if self.__memory[i] == item:
                counter += 1

        return counter

    # O(n), O(n), O(n)

    def find(self, item: Any) -> Any:

        for i in range(0, self.__count, 1):
            if self.__memory[i] == item:
                return i

        return -1

    # O(1), O(n), O(n)

    def is_empty(self) -> bool:
        return self.__count == 0

    def reverse(self, list: List) -> List:

        if List.is_empty():
            return list

        length = len(list)

        for i in range(0, length // 2):
            list[i], list[-1 - i] = list[-1 - i], list[i]

        return list

    # O(n), O(n), O(n)

    def sort(self, list: list, key=lambda obj: obj, order_by=lambda x, y: x > y) -> list:

        if not isinstance(list, list):
            raise TypeError()

        if self.__count == 0:
            return -1

        for i in range(0, self.__count - 1, 1):
            for j in range(0, self.__count - i - 1, 1):
                if order_by(key(self.__memory[j]), key(self.__memory[j + 1])):
                    self.__memory[j], self.__memory[j + 1] = self.__memory[j + 1], self.__memory[j]

        return list

    # O(n**2), O(n**2), O(n**2)


