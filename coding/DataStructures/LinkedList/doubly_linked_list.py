class Node:
    """
    Class Node contains a simple constructor an init method , where we say we have a value
    - every node is initialized with a value
    - every node is initialized with a next pointer(reference to another Node)
    """

    def __init__(self, value):
        self.value = value
        self.next = None  # every node when we create doesn't have next node reference
        self.prev = None  # doubly linked list


class DoublyLinkedList:
    """
    Linked list is another class utilizes the Node class.
    - Linked list has a head node( a beginning node - sset it to none in the beginning)
    """

    def __init__(self):
        self.head = None
        self.tail = None  # doubly linked list
        # self.size = 0

    # 9 O(n)
    def __repr__(self) -> str:
        """repr function this is gooing to traverse the list and print the values that are part of the list"""
        if self.head is None:
            return "[]"
        else:
            last = self.head
            return_string = f"[{last.value}"
            while last.next is not None:
                last = last.next
                return_string += f", {last.value}"
            return_string += "]"
            return return_string

    # 4 O(n)
    def __contains__(self, value):
        """checks if the value exists in a list"""
        last = self.head
        while last is not None:
            if last.value == value:
                return True
            last = last.next

        return False

    # 5 O(n)
    def __len__(self):
        """returns the length/size of the list"""

        last = self.head
        count = 0
        while last is not None:
            count += 1
            last = last.next
        return count

    # O(1) constant time #1
    def append(self, value):
        """adds a value to the end of the list"""
        if self.head is None:  # if the list is empty
            self.head = Node(value)
            self.tail = self.head

        else:
            last_node = Node(value)
            last_node.prev = self.tail
            self.tail.next = last_node
            self.tail = last_node

    # O(1) constant time #2
    def prepend(self, value):
        """adds a value to the beginning of the list"""

        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            first_node = Node(value)
            first_node.next = self.head
            self.head.prev = first_node
            self.head = first_node

    # 3 O(n) linear run time
    def insert(self, value, index):
        """inserts a value at a given index"""
        if index == 0:
            self.prepend(value)
        else:
            if self.head is None:
                raise ValueError("Index out of range")
            else:
                last = self.head
                for i in range(index - 1):
                    if last.next is None:
                        raise ValueError("Index out of range")
                    last = last.next
                new_node = Node(value)
                new_node.next = last.next  # point the new node to last.next node ref
                new_node.prev = last
                if last.next is not None:
                    last.next.prev = new_node
                last.next = new_node  # then point last to new_node

    # 6 O(n)
    def delete(self, value):
        """deletes a value from the list"""
        last = self.head
        print(last.value)
        if last is not None:
            if last.value == value:
                self.head = last.next  # if we are finding value already in the head
            else:
                while last.next:
                    if last.next.value == value:
                        if last.next.next is not None:
                            last.next.next.prev = last
                        last.next = last.next.next
                        break
                    last = last.next

    # 7 O(n)
    def pop(self, index):
        """removes the last value from the list"""
        if self.head is None:
            raise ValueError("Index out of range")
        else:
            last = self.head
            for i in range(index - 1):
                if last.next is None:
                    raise ValueError("Index out of range")
                last = last.next

            if last.next is None:  # edge case
                raise ValueError("Index out of range")
            else:
                if last.next.next is not None:
                    last.next.next.prev = last

                last.next = last.next.next

    # 8
    def get(self, index):
        """returns the value at a given index"""
        if self.head is None:
            raise ValueError("Index out of range")
        else:
            last = self.head
            for i in range(index):
                if last.next is None:
                    raise ValueError("Index out of range")
                last = last.next
            return last.value


if __name__ == "__main__":
    ll = DoublyLinkedList()
    # ll.append(1)  # 1
    # print(ll)
    # ll.append(2)
    # print(ll)
    # ll.append(3)
    # print(ll)
    # ll.append(4)
    # print(ll)

    # ll.prepend(0)  # 2
    # print(ll)
    # ll.prepend(-1)
    # print(ll)
    # # [-1, 0, 1, 2, 3, 4]
    # ll.insert(5, 5)  # 3
    # print(ll)
    # # [-1, 0, 1, 2, 3, 5, 4]
    # ll.pop(6)  # 4
    # print(ll)
    # # [-1, 0, 1, 2, 3, 5]

    # print(ll.get(2))  # 5
    # # 1
    # print(ll.get(4))
    # # 3
    # # print(ll.get(6))
    # #     Traceback (most recent call last):
    # #   File "C:\Users\abhis\Desktop\PythonDev\LearnPython\UnderstandPython\coding\DataStructures\LinkedList\linked_list.py", line 160, in <module>
    # #     print(ll.get(6))
    # #           ^^^^^^^^^
    # #   File "C:\Users\abhis\Desktop\PythonDev\LearnPython\UnderstandPython\coding\DataStructures\LinkedList\linked_list.py", line 136, in get
    # #     raise ValueError("Index out of range")
    # # ValueError: Index out of range
    # ll.delete(5)  # 6
    # print(ll)
    # # [-1, 0, 1, 2, 3]
    # ll.delete(-1)
    # # [0, 1, 2, 3]
    # print(ll.__contains__(3))  # True #7
    # print(ll.__contains__(-1))  # False
    # print(ll.__len__())  # 4 #8
    # $ python doubly_linked_list.py
    # [1]
    # [1, 2]
    # [1, 2, 3]
    # [1, 2, 3, 4]
    # [0, 1, 2, 3, 4]
    # [-1, 0, 1, 2, 3, 4]
    # [-1, 0, 1, 2, 3, 5, 4]
    # [-1, 0, 1, 2, 3, 5]
    # 1
    # 3
    # -1
    # [-1, 0, 1, 2, 3]
    # -1
    # True
    # False
    # 4

    ll.append(10)
    print(ll)
    ll.insert(20, 1)
    print(ll)
    ll.insert(30, 1)
    print(ll)
    ll.insert(40, 1)
    print(ll)
    ll.prepend(100)
    print(ll)
    ll.prepend(200)
    print(ll)
    ll.insert(300, 1)
    print(ll)
    ll.delete(20)
    print(ll)
    ll.delete(200)
    print(ll)
    ll.pop(1)
    print(ll)

# $ python doubly_linked_list.py
# [10]
# [10, 20]
# [10, 30, 20]
# [10, 40, 30, 20]
# [100, 10, 40, 30, 20]
# [200, 100, 10, 40, 30, 20]
# [200, 300, 100, 10, 40, 30, 20]
# 200
# [200, 300, 100, 10, 40, 30]
# 200
# [300, 100, 10, 40, 30]
