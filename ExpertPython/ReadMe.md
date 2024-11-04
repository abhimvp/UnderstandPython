## Intro

- In this , we will see expert level python features , how they work , how they implement , how we use them in python code
- How python code is actually ran and executed - python is interpreted programming language , althrough it's interprested , it's also compiled and turns it into a byte code
- compiler -> turns high level code to low level code(Byte code) understood by machine
- Interpreter -> takes some kind of code typically byte code , interprets and runs that code , translate it on the fly into machine code that is executed by our computer

## About Dunder/magic methods and python data model

- these dunder methods are part of [python data model](https://docs.python.org/3/reference/datamodel.html) -> here we can find all the double underscore methods that we can implement on our objects
- so we can actually implement whatever functionality we want using the upper level python syntax`p* 2` by implementing lower level dunder methods`__mul__`

## Metaclasses & How classes really work

- Now the property of an object essentially means that we can interact with it at run time

  - we can pass it around through parameters , through variables , we can store it , we can save it , we can modfiy it , we can interact -> that's what an object is

- But how is a class an object?
- so what we are getting into here with metaclasses is that the basic idea is a class defines the rules for an object , defines the attributes , parameters , methods & things can be performed , that's what class does for an object
  - what a metaclass does is define the rules for a class
    - so when you create a class , you will use the meta class to create it , this happens automatically , & that meta class defines how this class is created & that's the basic concept here
- so knowing this information , metaclasses can be very powerful , we can make the attributes and function names to capital let's see that as an example in `metaclasses4.py`

## Context Managers

- Context managers allow you to ensure a certain operation occurs on exit or crash from a certain block of code. This is useful for something like files, where it it essential that you close the file after it is opened.

## ToDO : locks and threads using contextmanagers - Learn
