# linked _list module

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    # arajin metods
    def __init__(self):
        self.start = None
    #erkrod metods
    def append(self, data):
        if not self.start:
            self.start = Node(data)
            return

        last = self.start
        while last.next is not None:
            last = last.next

        tmp_node = Node(data)
        last.next = tmp_node
        tmp_node.prev = last

    # errord metods
    def display(self):
        current = self.start
        while current is not None:
            print(current.data)
            current = current.next

    # 4 metods
    def is_empty(self) -> bool:
        return not self.start

    # 5 metods
    def prepend(self, data):
        if not self.start:
            self.start = Node(data)
            return

        tmp_node = Node(data)
        tmp_node.next = self.start
        self.start.prev = tmp_node
        self.start = tmp_node

    #6 metods
    def insert_after(self, target_data, data):
        if self.is_empty():
            raise ValueError("The list is empty!")

        found = self.start
        while found is not None:
            if found.data == target_data:
                break
            found = found.next

        if not found:
            raise ValueError(f"There is no element in the list: {data}!")

        tmp_node = Node(data)
        found_last = True if not found.next else False
        if found_last:
            found.next = tmp_node
            tmp_node.prev = found
        else:
            tmp_node.prev = found
            tmp_node.next = found.next
            found.next.prev = tmp_node
            found.next = tmp_node
    #7 metods
    def insert_before(self, target_data, data):
        if self.is_empty():
            raise ValueError("The list is empty!")

        found = self.start
        while found is not None:
            if found.data == target_data:
                break
            found = found.next

        if not found:
            raise ValueError(f"There is no element in the list: {data}!")

        tmp_node = Node(data)
        if found is self.start:
            self.prepend(data)
        else:
            tmp_node.next = found
            tmp_node.prev = found.prev
            found.prev.next = tmp_node
            found.prev = tmp_node
    # 8 metods
    def delete(self, data):
        if self.is_empty():
            raise ValueError("The list is empty!")

        found = self.start
        while found is not None:
            if found.data == data:
                break
            found = found.next

        if not found:
            raise ValueError(f"There is no element in the list: {data}!")

        if found is self.start:
            if found.next is None:
                self.start = None
            else:
                self.start = self.start.next
            return

        left, right = found.prev, found.next
        left.next = right
        right.prev = left
