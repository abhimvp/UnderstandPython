class YearReport:
    """Isolates all file system knowledge to the reporting class"""

    def export_year_report(self, name, year_salary):
        with open(name, "w") as file:
            file.write(f"Hello {name}, your year salary is {year_salary}")
