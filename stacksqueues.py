# Stack is LIFO, the first element out is the last element in
# Queue is FIFO, the first element out is the first element in

from abc import ABCMeta, abstractmethod


class CustomContainer(metaclass=ABCMeta):

    @abstractmethod
    def push(self, value):
        """
        A insert method for container
        :return:
        """

        pass

    @abstractmethod
    def pop(self):
        """
        A delete method for container
        :return:
        """

        pass

    @abstractmethod
    def is_empty(self):
        """
        Check if the container is empty
        :return:
        """

        pass


class CustomStack(CustomContainer):

    def __init__(self, n=0):

        self._stack = [None] * n
        self._top = -1
        self._stack_length = n

    def is_empty(self):

        if self._top == -1:
            return True

        else:
            return False

    def pop(self):

        if self.is_empty():
            # underflow error
            raise ValueError('the current stack is empty!')

        else:
            # 通过修改top指针的方式来pop，并不删减array的内容和长度
            self._top = self._top - 1

            return self._stack[self._top + 1]

    def push(self, value):

        self._top = self._top + 1

        if self._top == self._stack_length:
            # overflow error

            self._top = self._top - 1

            raise ValueError('reach the max length of stack')

        else:
            self._stack[self._top] = value

    def __repr__(self):

        return self._stack.__str__()


class CustomQueue(CustomContainer):

    def __init__(self, n=0):

        self._queue = [None] * n
        self._head = 0
        self._tail = 0
        self._queue_length = n
        self._is_full = False

    def push(self, value):

        if self._is_full:

            raise ValueError('the queue is full!')

        if self._tail + 1 == self._queue_length:
            next_tail = 0

        else:
            next_tail = self._tail + 1

        if next_tail == self._head:

            self._is_full = True

        self._queue[self._tail] = value
        self._tail = next_tail

    def pop(self):

        if self.is_empty():

            raise ValueError('the queue is empty !')

        else:

            pop_value = self._queue[self._head]

            if self._head + 1 == self._queue_length:
                self._head = 0

            else:
                self._head = self._head + 1

            self._is_full = False

            return pop_value

    def is_empty(self):

        if (self._head == self._tail) & (not self._is_full):

            return True

        else:

            return False

    def __repr__(self):

        return str(self._queue)
