# Dependency Injection

- Dependency injection is the key to decoupling code.
- In this [video](https://youtu.be/BdMO1IR-800?si=2BLf_d8x9RUKShai) you learn how to use DI and polymorphism to achieve the holy grail in software architecture: Adhering to the OPEN-CLOSED principle.

## Notes:

- Take a program that is tightly coupled , see why that is a problem and fix it with dependency injection.
- DI is needed when your code is spread over multiple classes or modules.
- problem:
  - json file with three employees with name and salary
  - class payroll.py has methods create_year_info that will load the json and create a year info report for each employee
  - running python main_problem.py file gives us three files with their yearly salary info - `Hello Abhi, your yearly salary is 26400.`
  - The class name payroll implies that it contains business logic , but it imports json , this class has knowledge of file systems and the json data format knowledge (`employee in data["employees"]`) everywhere & this is `a problem` why?
    - let's say instead of json , we provide excel with same employees name and different salary and now we need to import another library openpyxl and using load_workbook we take data from excel and we got to change code at every step , this is dangerous because if the class contains complex payroll logic instead of multiplying each salary by 12 & there is another problem business class payroll now has knowledge of excel structures.
- Now we have a task here , i will make the payroll class completely unaware of file systems and excel data structures , we will do this with dependency injection.
  - create a new module that will load the data - `dataloader.py`
  - add a class initializer to the payroll_solution class to accept a data loader object , here the class initializer takes & stores all the dependencies needed for the class to do it's job , we replace the excel code which allows to remove all import statements - has no knowledge of json or excel
  - by using DI the payroll_sol class is fully decoupled of any dependencies on the file system , json and excel libraries
