x: int = 1  # enforcing x should store integers only
# x = "abhi"  # gives errors that Type "Literal['abhi']" is not assignable
# to declared type "int"

from typing import List, Dict, Set

y: List[List[int]] = [[1, 2], [3, 4]]
# print(y)
z = [[1, 2], [3, 4]]
a: Dict[str, int] = {"a": 1, "b": 2}
b: Set[int] = {1, 2, 3, 4, 5}

## create our own types

Vector = List[float]
Vectors = List[Vector]


def foo(v: Vector) -> Vector:
    return v


print(foo([1.0, 2.0, 3.0]))

def foo_vectors(v: Vectors) -> Vectors:
    return v
print(foo_vectors([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]))

## optional types

from typing import Optional
def foo_optional(s: Optional[str]) -> str:
    if s is None:
        s = ""
    return s + "bar"

# Any type
from typing import Any
def foo_any(item: Any) -> str:
    return str(item) + "bar"

# sequence Type
from typing import Sequence # both the list and tuple count as a sequence , so accept any sequence
def foo_sequence(item: Sequence) :
    print( item , "bar")

foo_sequence([1, 2, 3])
foo_sequence((1, 2, 3))
# mapping Type
from typing import Mapping
def foo_mapping(item: Mapping) -> str:
    return str(item) + "bar"

# callable Type
from typing import Callable
# when do we use it? to accept a function as a parameter

def foo_callable(funct: Callable[[str],str]): 
    # the funct needs to be a function 7 have a one str parameter and str as return ty[pe]
    funct("bar")

# generics
from typing import TypeVar
T = TypeVar("T")
def foo_generic(item: T) -> T:
    return item
foo_generic(1)
foo_generic("abhi")
foo_generic([1, 2, 3])
foo_generic({"a": 1, "b": 2})

def get_item(lst: List[T], index: int) -> T:
    return lst[index]
