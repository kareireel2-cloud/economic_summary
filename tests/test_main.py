import pytest
import sys
from unittest.mock import patch, MagicMock
from main import render_report

def test_main_calls_correct_report(monkeypatch):
    """
    Проверяем, что main правильно парсит аргументы и 
    вызывает нужный метод у EconomicReport.
    """
    test_args = ["main.py", "--files", "f1.csv", "--report", "average_gdp"]
    monkeypatch.setattr(sys, "argv", test_args)


    with patch("main.EconomicReport") as MockReport:

        mock_instance = MockReport.return_value
        
        render_report()

        MockReport.assert_called_once_with(files=["f1.csv"])
        
        mock_instance.average_gdp.assert_called_once()

def test_main_invalid_report_choice(monkeypatch, capsys):
    """
    Проверяем, что argparse выдает ошибку, если отчета нет в choices.
    """
    test_args = ["main.py", "--files", "f1.csv", "--report", "unknown_report"]
    monkeypatch.setattr(sys, "argv", test_args)

    with pytest.raises(SystemExit):
        render_report()
    
    captured = capsys.readouterr()
    assert "invalid choice: 'unknown_report'" in captured.err

def test_main_missing_required_args(monkeypatch):
    """
    Проверяем ошибку, если забыли --files.
    """
    test_args = ["main.py", "--report", "average_gdp"]
    monkeypatch.setattr(sys, "argv", test_args)

    with pytest.raises(SystemExit):
        render_report()