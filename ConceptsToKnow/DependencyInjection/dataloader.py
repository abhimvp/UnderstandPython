# loads the data and will be responsible
# for all things that have to do with files and data formats
# lets start by creating excel data loader

from openpyxl import load_workbook

# same for json
import json


class ExcelDataLoader:
    """
    Has single method returns employees data from excel file
    - returns a list of tuples with name and salary
    - any knowledge of excel cells is hidden in this class
    """

    def load_employees(self):
        workbook = load_workbook(filename="employees.xlsx")
        worksheet = workbook.worksheets[0]
        rows = worksheet["A1:B3"]

        return [(name.value, salary.value) for name, salary in rows]


class JSONDataLoader:
    def load_employees(self):
        with open("employees.json") as file:
            data = json.load(file)

        return [
            (employee["name"], employee["salary"]) for employee in data["employees"]
        ]
