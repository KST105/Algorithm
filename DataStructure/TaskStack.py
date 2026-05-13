import datetime
from __future__ import annotations



class TaskStack:

    def __init__(self):
        self.__top = None
        self.__count = 0

    class ProjectTask:

        def __init__(self, description: str, due_date: datetime):

            self.description = description
            self.due_date = due_date

    class Node:

        def __init__(self, task: ProjectTask, prev: Node = None):
            self.task = task
            self.prev = prev

    def push(self, task: ProjectTask) -> None:
        node = TaskStack.Node(task)

        if not self.is_empty():
            node.prev = self.__top

        self.__top = node
        self.__count += 1

    def pop(self) -> ProjectTask:
        if self.is_empty():
            return None

        buff = self.__top.task
        self.__top = self.__top.prev
        self.__count -= 1

        return buff

    def peek(self) -> ProjectTask:
        if self.is_empty():
            return None

        return self.__top.task

    def is_empty(self) -> bool:
        return self.__count == 0


