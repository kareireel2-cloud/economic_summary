from src.parsing import AvgGdpReport
from tabulate import tabulate

class Utility:    
    @staticmethod
    def print_report(data:list, headers:list[str]):
        # headers - название колонок для отчёта
        print(tabulate(data, headers=headers,tablefmt='grid'))

class EconomicReport:
    def __init__(self,files):
        self.files = files

    # В этом классе можно дополнять логику для других видов отчётов.
    def average_gdp(self):  
        data = AvgGdpReport.avg_gdp_list(files=self.files)
        headers = ['country','gdp']
        Utility.print_report(data=data,headers=headers)