from src import EconomicReport
import argparse

def render_report():
    '''
    Чтобы дополнить скрипт новым видом отчёта надо:
    1)Дополнить список aviable_reports в этом файле названием нового отчёта
    2)в src/parcing создать новый класс,
        в котором будет прописана логика парсинга искомых данных.
    3)в src/report в классе дополнить новый метод с тем же названием
        отчёта что и в пункте 1, в котором будут прописаны:
        headers - название колонок,
        data - спарсеные данные для отчёта.
    '''
    parser = argparse.ArgumentParser()
    aviable_reports = ['average_gdp']

    parser.add_argument("--files", nargs='+',type=str, required=True)
    parser.add_argument("--report", type=str, choices= aviable_reports)

    args = parser.parse_args()

    files = args.files
    report_type = args.report
    
    report = EconomicReport(files=files)
    func = getattr(report, report_type )

    if callable(func):
        func()

def main():
    render_report()
 
if __name__ == "__main__":    
    main()