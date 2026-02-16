# Economic Summary Tool 

Консольное приложение для анализа экономических показателей из CSV-файлов. Скрипт объединяет данные из нескольких источников и принимает тип требуемого отчёта, пока что доступен отчёт среднего ВВП "average_gdp", после чего выводит требуемый отчёт из данных с источников.

## Установка

1. **Клонируйте репозиторий:**
```bash
   git clone [https://github.com/kareireel2-cloud/economic_summary.git](https://github.com/kareireel2-cloud/economic_summary.git)
   cd economic_summary
```

2. **Создайте виртуальное окружение :**
``` bash
    python -m venv venv
    source venv/Scripts/activate  # Для Windows
    # или
    source venv/bin/activate      # Для macOS/Linux
```
    
3. **Установите зависимости:**
``` bash
    pip install tabulate #для тестирования ещё установить pytest
    # или через uv
    uv sync
```
## Запуск

Скрипт принимает на вход список CSV-файлов и тип отчета.

**Команда для запуска:**

``` Bash
python main.py --files economic1.csv economic2.csv --report average_gdp
```

### Параметры:

- `--files`: Пути к одному или нескольким файлам через пробел.
    
- `--report`: Тип отчета (на данный момент доступен `average_gdp`).