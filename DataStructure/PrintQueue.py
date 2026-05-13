class  PrintQueue:

    class PrintDocument:

        def __init__(self, title: str, number_of_pages: int):

            self.title = title
            self.number_of_pages = number_of_pages


    class Node:

        def __init__(self, document: PrintDocument, prev: Node = None, next: Node = None):

            self.document = document
            self.prev = prev
            self.next = next


    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def enqueue(self, document: PrintDocument) -> None:

        if self.is_empty():
            self.__head = document


    def dequeue():
        pass

    def peek():
        pass

    def count(self) -> int:
        return self.__count

    def is_empty(self) -> bool:
        return self.__count == 0