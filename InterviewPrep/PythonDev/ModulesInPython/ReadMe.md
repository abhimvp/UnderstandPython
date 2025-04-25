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

## Packages in python

- let's say we want to add more functionality and we create a separate a folder called `shopping` and create a `shopping_cart.py` file.
- Now we want to use that shopping_cart in our example_main.py file , how do we do that? , even if we try to import shopping_cart as we did with utility , we get

```bash
abhis@Tinku MINGW64 ~/Desktop/PythonDev/LearnPython/UnderstandPython/InterviewPrep/PythonDev/ModulesInPython (main)
$ python example_main.py
Traceback (most recent call last):
  File "C:\Users\abhis\Desktop\PythonDev\LearnPython\UnderstandPython\InterviewPrep\PythonDev\ModulesInPython\example_main.py", line 2, in <module>
    import shopping_cart
ModuleNotFoundError: No module named 'shopping_cart'
```

- what we have created above `shopping` folder is what we call a `package` , a package is a folder containing modules. so for us to use the shopping-cart module from shopping package we do `import shopping.shopping_cart`
  - when we run example_main.py file , it creates a `__pycache__` for shopping_cart.py as we are trying to import this module into the main.py file.

```bash
$ python example_main.py
<module 'example_utility' from 'C:\\Users\\abhis\\Desktop\\PythonDev\\LearnPython\\UnderstandPython\\InterviewPrep\\PythonDev\\ModulesInPython\\example_utility.py'>
<module 'shopping.shopping_cart' from 'C:\\Users\\abhis\\Desktop\\PythonDev\\LearnPython\\UnderstandPython\\InterviewPrep\\PythonDev\\ModulesInPython\\shopping\\shopping_cart.py'>
```

- but usually we have this `__init__.py` file inside a package root , because the interpreter will read that file and recognizes this is a package.(In projects)
- **Different ways to import the modules**:

  - using `from` , like `from package.module_name import function_we_want_to_use`
  - same with utility as well , we do `from example_utility import multiply, add` - a nice way to clean up our code.

- as we build through projects or files , we see this `if __name__ == '__main__':` , when working with python , we should know what it does: - let's add `print(__name__)` in our modules and see what it prints.
  - when we run our `example_main.py` file here , our interpreter goes line by line , it imports utility file by going to that file and runs that file line by line in there and that's why we see `example_utility` being printed on screen when we run main.py, similarly it is same for shopping_cart.
  - if we add same `print(__name__)` in example_main.py , we see `__main__` get's printed.but why is that? not `example_main` likewise?
  - The name `__main__` is specifically **given to the file we run** , that's why we see `if __name__ == '__main__': print("example_main.py")` , it prints the following when we run main.py and it's not gonna print example_utility.py when we include something like above in utility.py file. As it is not the file being run and not the main file.

```bash
$ python example_main.py
example_utility
shopping.shopping_cart
6
5
['shoes']
# __main__
$ python example_main.py
example_utility
shopping.shopping_cart
6
5
['shoes']
This is the main file - example_main.py
```

- we will use this `if __name__ == '__main__'` in a file to make sure that we don't want to run the following functions unless it's a main_file.
- if we keep our multiply,add func under the above line of code we see the following error when we run example_main.py:

```bash
$ python example_main.py
example_utility
Traceback (most recent call last):
  File "C:\Users\abhis\Desktop\PythonDev\LearnPython\UnderstandPython\InterviewPrep\PythonDev\ModulesInPython\example_main.py", line 2, in <module>
    from example_utility import multiply, add
ImportError: cannot import name 'multiply' from 'example_utility' (C:\Users\abhis\Desktop\PythonDev\LearnPython\UnderstandPython\InterviewPrep\PythonDev\ModulesInPython\example_utility.py)
```

- we aren't able to import because we aren't running the example_utility as main file and that's why example_main couldn't find funcs.

- all we are saying with `__name__ == __main__` , if this is the file being run ( importing is different - remember) , then do something - run those lines of code under it.
