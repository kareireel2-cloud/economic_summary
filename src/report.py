from src.parsing import AvgGdpData
from tabulate import tabulate

def _print_report(data:list, headers:list[str]):
        print(tabulate(data, headers=headers,tablefmt='grid'))    
            
class EconomicReport:
    # В этом классе можно дополнять логику для других видов отчётов.    
    def __init__(self,files):
        self.files = files

    def average_gdp(self):  
        data = AvgGdpData.avg_gdp_list(files=self.files)
        headers = ['country','gdp']
        _print_report(data=data, headers=headers)