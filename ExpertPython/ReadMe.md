## Intro

- In this , we will see expert level python features , how they work , how they implement , how we use them in python code
- How python code is actually ran and executed - python is interpreted programming language , althrough it's interprested , it's also compiled and turns it into a byte code
- compiler -> turns high level code to low level code(Byte code) understood by machine
- Interpreter -> takes some kind of code typically byte code , interprets and runs that code , translate it on the fly into machine code that is executed by our computer

## About Dunder/magic methods and python data model

- these dunder methods are part of [python data model](https://docs.python.org/3/reference/datamodel.html) -> here we can find all the double underscore methods that we can implement on our objects
- so we can actually implement whatever functionality we want using the upper level python syntax`p* 2` by implementing lower level dunder methods`__mul__`
