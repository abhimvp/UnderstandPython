class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# queue - FIFO principle - First In First Out
# enqueue - put at the rear end of the queue
# dequeue - take element from the front
# Front 1 2 3 4 5 Rear -> rear add elements , front remove elements - basic idea
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None  # append new elements here
        self.size = 0

    def __len__(self):
        return self.size

    def __repr__(self):
        if self.front is None:
            return "Queue is empty"
        current = self.front
        queue = []
        while current:
            queue.append(str(current.value))
            current = current.next
        return " -> ".join(queue)

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        self.size += 1

    def dequeue(self):
        if self.front is None:
            raise Exception("Queue is empty")
        dequeue_node = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return dequeue_node

    def peek(self):
        if self.front is None:
            raise Exception("Queue is empty")
        return self.front.value

    def is_empty(self):
        if self.front is None:
            return True
        return False


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    print(queue)
    print(queue.peek())
    print(queue.dequeue())
    print(queue.peek())
    print(queue.is_empty())
    print(queue.__len__())
    print(queue)
