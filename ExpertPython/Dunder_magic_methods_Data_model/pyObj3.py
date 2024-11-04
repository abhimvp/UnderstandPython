from queue import Queue
import inspect

# q = Queue()  # queue object
# print(q)  # <queue.Queue object at 0x000001F1565D9EE0>
# # above it doesn't print in a repr way , why is that?

# print(inspect.getsource(Queue))  # prints the source code of the Queue class , we can
# it doesn't have the repr method built-in

# so we can create our own repr method

from queue import Queue as q


class Own_Queue(q):

    def __repr__(self):
        return f"Queue({self._qsize()})"

    def __add__(self, item):
        # # Put a new item in the queue
        # def _put(self, item):
        # self.queue.append(item)
        self.put(item)

    def __sub__(self, item):
        # # Remove an item from the queue
        # def _get(self):
        # return self.queue.pop(0)
        self.get()


qu = Own_Queue()
qu + 1  # Queue(1)
qu + 2  # Queue(2)
qu + 3  # Queue(3)
qu - 0  # Queue(2)
print(qu)  # Queue(1)
