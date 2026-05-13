from __future__ import annotations



class PersonList:

    class PersonCard:

        def __init__(self, Name: str, Age: int, Occupation: str):
            self.Name = Name
            self.Age = Age
            self.Occupation = Occupation

    class Node:

        def __init__(self, person: PersonCard, next: Node = None):
            self.person = person
            self.next = next

    def __init__(self):
        self.__count = 0
        self.__head = None

    def append_person(self, person: PersonCard) -> None:

        node = self.Node(person=person, next=None)

        if self.is_empty():
            self.__head = node
            self.__count += 1

            return

        iterator = self.__head

        while iterator.next is not None:
            iterator = iterator.next

        iterator.next = node
        self.__count += 1

        return None

    def add_person(self, person: PersonCard) -> None:

        node = self.Node(person=person, next=self.__head)
        self.__head = node
        self.__count += 1

        return None

    def insert_person_at(self, position: int, person: PersonCard) -> None:

        if position < 0 or position > self.__count:
            raise IndexError(f"Позиция {position} выходит за границы")

        node = self.Node(person=person, next=None)

        if self.is_empty():
            self.__head = node
            self.__count += 1
            return

        if position == 1:
            self.add_person(person)
            self.__count += 1
            return

        iterator = self.__head
        iiterator = 1

        while iiterator <= position-1 and iterator.next is not None:
            iiterator += 1
            iterator = iterator.next

        node.next = iterator.next
        iterator.next = node

        self.__count += 1

    def remove_first_person(self):

        if self.is_empty():
            return None

        buff = self.__head.person
        self.__head =  self.__head.next
        self.__count -= 1

        return buff

    def remove_last_person(self):

        if self.is_empty():
            return None

        if self.__count == 1:
            buff = self.__head.person
            self.__head = None
            self.__count = 0

            return buff

        iterator = self.__head

        while iterator.next.next is not None:
            iterator = iterator.next

        buff = iterator.next.person
        iterator.next = None
        self.__count -= 1

        return buff

    def clear_all(self):
        self.__head = None
        self.__count = 0

        return

    def remove_person(self, person: PersonCard):

        if self.is_empty():
            return None

        if self.__head.person == person:
            self.__head = self.__head.next
            self.__count -= 1

            return


        iterator = self.__head

        while iterator.next is not None:
            if iterator.next.person == person:
                iterator.next = iterator.next.next
                self.__count -= 1

                return

            iterator = iterator.next

        return None

    def find_person(self, person: PersonCard) -> Any:

        if not self.__head:
            return None

        iterator = self.__head

        iiterator = 1

        while iterator is not None:
            if iterator.person == person:
                return iterator.person, iiterator
            iterator = iterator.next
            iiterator += 1

        return None

    def total_people(self) -> int:
        return self.__count

    def is_empty(self) -> bool:
        return self.__count == 0
