import json


class Payroll:
    def create_year_info(self):
        with open("employees.json") as file:
            data = json.load(file)

        for employee in data["employees"]:
            year_salary = employee["salary"] * 12

            with open(employee["name"], "w") as file:
                file.write(
                    f"Hello {employee['name']}, your yearly salary is {year_salary}."
                )
