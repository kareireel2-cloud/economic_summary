import pytest
import csv
from src.parsing import AvgGdpData

@pytest.fixture
def create_csv_files(tmp_path):
    file1 = tmp_path / "data1.csv"
    file2 = tmp_path / "data2.csv"

    with open(file1, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['country', 'gdp'])
        writer.writeheader()
        writer.writerow({'country': 'Russia', 'gdp': '100'})
        writer.writerow({'country': 'USA', 'gdp': '200'})
        writer.writerow({'country': 'Russia', 'gdp': '200'})

    with open(file2, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['country', 'gdp'])
        writer.writeheader()
        writer.writerow({'country': 'USA', 'gdp': '400'})

    return [str(file1), str(file2)]

def test_avg_gdp_calculation(create_csv_files):
    '''
    Проверка на правильность расчёта среднего gdp.
    '''
    files = create_csv_files
    result = AvgGdpData.avg_gdp_list(files)
    
    expected = [
        ['USA', 300.0],
        ['Russia', 150.0]
    ]
    
    assert result == expected

def test_invalid_extension(tmp_path):
    txt_file = tmp_path / "test.txt"
    txt_file.write_text("some data")
    
    result = AvgGdpData.avg_gdp_list([str(txt_file)])
    assert result == []

def test_file_not_found():
    result = AvgGdpData.avg_gdp_list(["non_existent.csv"])
    assert result == []

def test_sorting(tmp_path):
    '''Проверка на правильную сортировку.'''
    file_path = tmp_path / "sort_test.csv"
    with open(file_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['country', 'gdp'])
        writer.writeheader()
        writer.writerow({'country': 'A', 'gdp': '10'})
        writer.writerow({'country': 'B', 'gdp': '50'})
        writer.writerow({'country': 'C', 'gdp': '30'})

    result = AvgGdpData.avg_gdp_list([str(file_path)])
    
    assert result[0][0] == 'B'
    assert result[2][0] == 'A'