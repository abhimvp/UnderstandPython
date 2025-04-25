# Modules in Python - how to organize code

- Initially we wrote our code in .py file
- Then we started writing the code in `f(x)` functions, so that we can re-use it whenever we want.
- And we have this `class` where we can create our own data types from what python already provided us to represent real-world entities or objects.
- also functional programming too. All of this to keep our code clean & more maintainable and organized.
- In real time projects we can't have one file with lots of lines of code , so how we stay organized?
- which is `modules` - a way for us to organize code/files.
- similar to classes we want to divide our code into chunks.
- a `__pycache__` file is created every time we run a file(main.py or whatever.py) which has import statements.
  - we can see a `__pycache__` folder got created inside it we see a `example_utility.cpython-312.pyc` file, after we ran example_main.py which consists only the import of example_utility.
  - `pyc` means it's using c python interpreter , .pyc is a compiled file , next i run example_main.py file , it loads the compiled version instead of main file example_utility.py , because nothing has changed init. This makes things faster when we run example_main.py , that's what caching is.
  - Here the example_utility.py is a `module`, so by using import statements between modules we're able to use functionality between different files.

```bash
abhis@Tinku MINGW64 ~/Desktop/PythonDev/LearnPython/UnderstandPython/InterviewPrep/PythonDev/ModulesInPython (main)
$ python example_main.py
<module 'example_utility' from 'C:\\Users\\abhis\\Desktop\\PythonDev\\LearnPython\\UnderstandPython\\InterviewPrep\\PythonDev\\ModulesInPython\\example_utility.py'>
```
