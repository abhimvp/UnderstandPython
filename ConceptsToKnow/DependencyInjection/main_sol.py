from payroll_solution import PayrollSolution
from dataloader import ExcelDataLoader, JSONDataLoader
from reporting import YearReport

data_loader_obj = ExcelDataLoader()
data_loader_obj_json = JSONDataLoader()
year_reporting = YearReport()
payroll = PayrollSolution(data_loader_obj_json, year_reporting)
payroll.create_year_info()
