# Dynamically typed language - we don't have to declare the type at all when
# declaring a variable.
n = 0
print("n = ", n)
n = "abc"
print("n = ", n)

# multiple assignment
n, m = 0, "abc"
n, m, z = 0.125, "abc", False
print(n, m, z)

# Increment
n = 0
n += 1  # n = n + 1
print(n)

# None is null (absence of value)
n = 4
n = None
print("n = ", n)

# If statement - don't need parentheses or curly braces
n = 1
if n > 2:
    n -= 1
elif n == 2:
    n *= 2
else:
    n += 2

# parenthesis needed for multi-line conditions
# and = &&
# or = ||
n, m = 1, 2

if (n > 2 and n != m) or n == m:
    n += 1

# while loops are similar
n = 0
while n < 5:
    print(n)
    n += 1
print("while loop ended")
# Looping from i = 0 to i = 4
for i in range(5):
    print(i)
print("for loop ended")
# Looping from i = 2 to i = 5
for i in range(2, 6):
    print(i)
print("for loop ended")
# Looping from i = 5 to i = 2
for i in range(5, 1, -1):
    print(i)
print("for loop ended")

# Divide by integer is float by default
print(5 / 2)  # 2.5
# division is decimal by default
print(5 // 2)  # 2 # double slash rounds down
print(-3 // 2)  # -2
# rounds down and returns the largest integer less than or equal to a given number
print(int(-3 / 2))  # -1
# modulo
print(10 % 3)  # 1
print(-10 % 3)  # 2
# math helpers
import math

print(math.floor(3 / 2))  # 1.0
print(math.ceil(3 / 2))  # 2.0
print(math.sqrt(2))  # 1.4142135623730951
print(math.pow(2, 3))  # 8.0
print(math.fmod(-10, 3))  # -1.0 (10 mod 3
print(math.fabs(-2))  # 2.0
print(math.factorial(5))  # 120

# max or min
print(max(1, 2, 3))  # 3
print(min(1, 2, 3))  # 1
print(max([1, 2, 3]))  # 3
print(min([1, 2, 3]))  # 1
float("inf")  # infinity
float("-inf")  # -infinity
print(math.pow(2, 200))  # float infinity
# python numbers are infinite so they never overflow
print(math.pow(2, 200) < float("inf"))  # True
# arrays (called lists in python)
array = [1, 2, 3]
print(array[0])  # 1
array[0] = "string"  # type: ignore
print(array)  # ['string', 2, 3]
# can be used as a stack
array.append(4)
print(array)  # ['string', 2, 3, 4]
array.pop()
print(array)  # ['string', 2, 3]
array.insert(1, 7)  # O(n) operation
print(array)  # ['string', 7, 2, 3]
array[0] = 0  # constant time
print(array)  # [0, 7, 2, 3]

# -1 indicates not found
print(array.index(7))  # 1
print(array.index(7, 1))  # 1
# print(array.index(7, 2))  # -1

# Initialize array with 0s
array = [0] * 5
print(array)  # [0, 0, 0, 0, 0]
# Initialize array with 1s
array = [1] * 5
print(array)  # [1, 1, 1, 1, 1]
print(len(array))  # 5
print(array[3])  # 1
print(array[-1])  # 1
print(array[-2])  # 1
# Sublists (starting index is inclusive, ending index is exclusive)
print(array[0:2])  # [1, 1]
print(array[:2])  # [1, 1]
# unpacking
a, b, c = [1, 2, 3]
print(a, b, c)  # 1 2 3
# Looping through arrays
nums = [1, 2, 3]
for i in range(len(nums)):
    print(nums[i])
print("for loop ended")
# without index
for n in nums:
    print(n)
print("for loop ended")
# enumerate - with index and value
for i, n in enumerate(nums):
    print(i, n)
print("for loop ended")
# Loop through multiple arrays simultaneously with unpacking
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)
print("for loop ended")
# Reverse
nums = [1, 2, 3]
nums.reverse()
print(nums)  # [3, 2, 1]
# Sorting
array = [5, 4, 7, 3, 8]
array.sort()
print(array)  # [3, 4, 5, 7, 8]
array.sort(reverse=True)
print(array)  # [8, 7, 5, 4, 3]
print(sorted(array))  # [3, 4, 5, 7, 8]
print(sorted(array, reverse=True))  # [8, 7, 5, 4, 3]
# Custom sort by second element
array = [(2, 5), (1, 8), (4, 4), (3, 3)]
array.sort(key=lambda x: x[1])
print(array)  # [(4, 4), (2, 5), (3, 3), (1, 8)]
# List comprehension
array = [i for i in range(5)]
print(array)  # [0, 1, 2, 3, 4]
# 0^2, 1^2, 2^2, 3^2, 4^2
array = [i * i for i in range(5)]
print(array)  # [0, 1, 4, 9, 16]
# with conditions
even = [i for i in range(5) if i % 2 == 0]
print(even)
odd = [i for i in range(5) if i % 2 == 1]
print(odd)  # [1, 3]
# string lists
s = "abc"
print(s[0:2])  # ab
# lists can be modified
K = list(s)
K[0] = "A"
s = "".join(K)
print(s)  # Abc
# 2-D lists
array = [[0] * 4 for i in range(4)]
print(array)  # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
array[0][1] = 1
print(array)  # [[0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# valid numeric strings can be converted
print(int("123"))  # 123
print(str(123))  # '123'
print(int("123") + int("123"))  # 246
print(str(123) + str(123))  # '123123'
# sets - no duplicates allowed
mySet = set()
mySet.add(1)
mySet.add(2)
print(mySet)  # {1, 2}
print(len(mySet))  # 2
print(1 in mySet)  # True
print(2 in mySet)  # True
print(3 in mySet)  # False
# rare cases you may need the ASCII value of a char
print(ord("a"))  # 97
print(ord("b"))  # 98
# combine list of strings (with an empty string delimitor)
strings = ["ab", "cd", "ef"]
print("".join(strings))  # abcdef
# queue (double ended queue)
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
print(queue)
queue.popleft()
print(queue)
queue.appendleft(1)
print(queue)
queue.pop()
print(queue)  # [1]
# hashmap (aka dict)
myMap = {}
myMap["alice"] = 88
myMap["bob"] = 77
print(myMap)  # {'alice': 88, 'bob': 77}
print(len(myMap))  # 2
myMap["alice"] = 80
print(myMap["alice"])  # 80
print("alice" in myMap)  # True
myMap.pop("alice")
print("alice" in myMap)  # False
# list to set
print(set([1, 2, 3]))  # {1, 2, 3}
# set comprehension
mySet = {i for i in range(5)}
print(mySet)  # {0, 1, 2, 3, 4}
# set operations
print({1, 2, 3}.union({2, 3, 4}))  # {1, 2, 3, 4}
print({1, 2, 3}.intersection({2, 3, 4}))  # {2, 3}
print({1, 2, 3}.difference({2, 3, 4}))  # {1}
print({1, 2, 3}.symmetric_difference({2, 3, 4}))  # {1, 4}
# Tuples are like arrays but immutable
tup = (1, 2, 3)
print(tup)  # (1, 2, 3)
print(tup[0])  # 1
print(tup[-1])  # 3
# can't modify
# tup[0] = 1 # TypeError
# can be used as key for hash map/set
myMap = {(1, 2): 3}
print(myMap[(1, 2)])  # 3
# dict comprehension
myMap = {i: 2 * i for i in range(3)}
print(myMap)  # {0: 0, 1: 2, 2: 4}
# looping through maps
myMap = {"alice": 90, "bob": 70}
for key in myMap:
    print(key, myMap[key])

# alice 90
# bob 70
for val in myMap.values():
    print(val)

    # 90
    # 70
for key, val in myMap.items():
    print(key, val)

# alice 90
# bob 70
# Heaps
import heapq

# under the hood are arrays
minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)
print(minHeap[0])  # 2 - min values is always at index 0
while len(minHeap):
    print(heapq.heappop(minHeap))

# 2
# 3
# 4
# no max heaps by default, work around for that
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)
while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))

# -4
# -3
# -2
# build heap from initial values
arr = [2, 1, 8, 4, 5]
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr))

# 1
# 2
# 4
# 5
# 8


# Functions
def myFunction(n, m):
    return n * m


print(myFunction(3, 4))  # 12


# nested functions have access to outer variables
def outer(a, b):
    c = "c"

    def inner():
        return a + b + c

    return inner()


print(outer("a", "b"))  # abc


# can modify objects but not reassign unless using nonlocal keyword
def double(array, val):
    def helper():
        # modifying array works
        for i, n in enumerate(array):
            array[i] *= 2
        # modifying val doesn't work
        # val *= 2
        # can't reassign outside of the helper function
        # val = 2
        nonlocal val
        val *= 2

    helper()
    print(array, val)


nums = [1, 2, 3]
val = 3
double(nums, val)

# double([1, 2, 3], 6)


# class
class MyClass:
    # constructor
    def __init__(self, nums):
        """self is passed into evry method of class"""
        # create member variables
        self.nums = nums
        self.size = len(nums)

    # self key word required as param
    def getLength(self):
        return self.size

    def getDoubleLength(self):
        return 2 * self.getLength()
        # return 2 * self.size


myObj = MyClass([1, 2, 3])
print(myObj.getLength())  # 3
print(myObj.getDoubleLength())  # 6
