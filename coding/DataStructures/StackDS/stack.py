# stack is a data structure which has push and pop operations & peek to look at the top element ,
# print the whole stack , iterate through it , operates through LIFO principle
# Last in first out , element added last in to the stack is the first one to processed

# stack will be based around node class


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def __len__(self):
        return self.size

    # O(n)
    def __repr__(self):
        items = []
        current_item = self.top
        while current_item is not None:
            items.append(str(current_item.value))
            current_item = current_item.next

        return "->".join(items)

    # O(1)
    def push(self, value):
        """Adds item into the stack"""
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    # O(1)
    def pop(self):
        """Returns the item"""
        if self.top is None:
            raise Exception("Stack is empty")
        else:
            pop_node = self.top
            self.top = self.top.next
            self.size -= 1
            return pop_node.value

    def peek(self):
        if self.top is None:
            raise Exception("Stack is empty")
        else:
            return self.top.value

    def is_empty(self):
        return self.top is None


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack)
    print(stack.pop())
    print(stack)
    print(stack.peek())
    print(stack.is_empty())
    print(stack.pop())
    print(stack.pop())
    print(stack.is_empty())
