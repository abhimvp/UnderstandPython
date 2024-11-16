class Node:
    """
    Class Node contains a simple constructor an init method , where we say we have a value
    - every node is initialized with a value
    - every node is initialized with a next pointer(reference to another Node)
    """

    def __init__(self, value):
        self.value = value
        self.next = None  # every node when we create doesn't have next node reference


class LinkedList:
    """
    Linked list is another class utilizes the Node class.
    - Linked list has a head node( a beginning node - sset it to none in the beginning)
    """

    def __init__(self):
        self.head = None
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

    # O(n) linear time #1
    def append(self, value):
        """adds a value to the end of the list"""
        if self.head is None:  # if the list is empty
            self.head = Node(value)

        else:
            last = self.head
            while last.next:  # traversing the list until last.next is None
                last = last.next
            # goes until there is no next value and adds the new value at the last node
            last.next = Node(value)

    # O(1) constant time #2
    def prepend(self, value):
        """adds a value to the beginning of the list"""
        first_node = Node(value)
        first_node.next = self.head
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
    ll = LinkedList()
    ll.append(1)  # 1
    print(ll)
    ll.append(2)
    print(ll)
    ll.append(3)
    print(ll)
    ll.append(4)
    print(ll)

    ll.prepend(0)  # 2
    print(ll)
    ll.prepend(-1)
    print(ll)
    # [-1, 0, 1, 2, 3, 4]
    ll.insert(5, 5)  # 3
    print(ll)
    # [-1, 0, 1, 2, 3, 5, 4]
    ll.pop(6)  # 4
    print(ll)
    # [-1, 0, 1, 2, 3, 5]

    print(ll.get(2))  # 5
    # 1
    print(ll.get(4))
    # 3
    # print(ll.get(6))
    #     Traceback (most recent call last):
    #   File "C:\Users\abhis\Desktop\PythonDev\LearnPython\UnderstandPython\coding\DataStructures\LinkedList\linked_list.py", line 160, in <module>
    #     print(ll.get(6))
    #           ^^^^^^^^^
    #   File "C:\Users\abhis\Desktop\PythonDev\LearnPython\UnderstandPython\coding\DataStructures\LinkedList\linked_list.py", line 136, in get
    #     raise ValueError("Index out of range")
    # ValueError: Index out of range
    ll.delete(5)  # 6
    print(ll)
    # [-1, 0, 1, 2, 3]
    ll.delete(-1)
    # [0, 1, 2, 3]
    print(ll.__contains__(3))  # True #7
    print(ll.__contains__(-1))  # False
    print(ll.__len__())  # 4 #8
