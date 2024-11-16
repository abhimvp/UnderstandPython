class PayrollSolution:
    def __init__(self, data_loader, reporting):
        self.data_loader = data_loader
        self.reporting = reporting

    def create_year_info(self):
        employees = self.data_loader.load_employees()

        for name, salary in employees:
            year_salary = salary * 12

            self.reporting.export_year_report(name, year_salary)
