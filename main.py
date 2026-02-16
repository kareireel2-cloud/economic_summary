import argparse
from src import EconomicReport


def main():
    
    parser = argparse.ArgumentParser()

    parser.add_argument("--files", nargs='+',type=str, required=True)
    parser.add_argument("--report", type=str, choices=['average_gdp'])

    args = parser.parse_args()

    files = args.files
    report_type = args.report
    report = EconomicReport(files=files)
    
    func = getattr(report, report_type )

    if callable(func):
        func()


if __name__ == "__main__":    
    main()