# linked _list module

class Node:
    def __init__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None


class LinkedList:
    def __init__(self):
        self.__start = None

    def append(self, data):
        if not self.__start:
            self.__start = Node(data)
            return

        last = self.__start
        while last.__next is not None:
            last = last.__next

        tmp_node = Node(data)
        last.__next = tmp_node
        tmp_node.__prev = last

    def display(self):
        current = self.__start
        while current is not None:
            print(current.__data)
            current = current.__next

    def is_empty(self) -> bool:
        return not self.__start

    def prepend(self, data):
        if not self.__start:
            self.__start = Node(data)
            return

        tmp_node = Node(data)
        tmp_node.__next = self.__start
        self.__start.__prev = tmp_node
        self.__start = tmp_node

    def insert_after(self, target_data, data):
        if self.is_empty():
            raise ValueError("The list is empty!")

        found = self.__start
        while found is not None:
            if found.__data == target_data:
                break
            found = found.__next

        if not found:
            raise ValueError(f"There is no element in the list: {data}!")

        tmp_node = Node(data)
        found_last = True if not found.__next else False
        if found_last:
            found.__next = tmp_node
            tmp_node.__prev = found
        else:
            tmp_node.__prev = found
            tmp_node.__next = found.__next
            found.__next.__prev = tmp_node
            found.__next = tmp_node

    def insert_before(self, target_data, data):
        if self.is_empty():
            raise ValueError("The list is empty!")

        found = self.__start
        while found is not None:
            if found.__data == target_data:
                break
            found = found.__next

        if not found:
            raise ValueError(f"There is no element in the list: {data}!")

        tmp_node = Node(data)
        if found is self.__start:
            self.prepend(data)
        else:
            tmp_node.__next = found
            tmp_node.__prev = found.__prev
            found.__prev.__next = tmp_node
            found.__prev = tmp_node

    def delete(self, data):
        if self.is_empty():
            raise ValueError("The list is empty!")

        found = self.__start
        while found is not None:
            if found.__data == data:
                break
            found = found.__next

        if not found:
            raise ValueError(f"There is no element in the list: {data}!")

        if found is self.__start:
            if found.__next is None:
                self.__start = None
            else:
                self.__start = self.__start.__next
            return

        left, right = found.__prev, found.__next
        left.__next = right
        right.__prev = left


        left, right = found.prev, found.next
        left.next = right
        right.prev = left
