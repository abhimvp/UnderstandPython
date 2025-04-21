# Functional Programming

- functional programming is all about separation of concerns , it's all about packaging our code into separate chunks so that everything is well organized.
- each piece of code or part is concerned about it itself that it's god at.
- separate data and functions.
- pure functions - Two Rules:
  - given the same input [1,2,3] -> func() -> gives us the same output [2,4,6] - `every time`
  - A function should not produce any side effects , side effects are things functions does that affect the outside world.
    - example like if we print something inside a function will affect outside world in a way it displays on screen (which we don't want) & trying to access a variable which is outside of scope..etc.
- map()
  - map automatically runs the func for us and loops through the iterable & returns a new map object , that we can convert to a list or tuple
- filter()
- zip()
- reduce()
- lambda expressions - are one time anonymous functions that you don't need more than once
- list comprehensions
- set & dictionary comprehensions
