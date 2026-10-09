def parse_record(line: str) -> dict:
    '''
    Разбирает строки журнала и определяет ошибку
    '''
    if not line.strip():
        raise ValueError('Пустая строка')
    parts = line.split(';')
    if len(parts) != 3:
        raise ValueError(f'Ожидалось 3 поля, получено {len(parts)}')
    city, temp, date = parts
    if not city.strip() or not date.strip():
        raise ValueError("Город или дата не могут быть пустыми")
    try:
        temp = float(temp)
    except ValueError:
        raise ValueError(f'Температура {temp} не является числом')
    return {
        "city": city.strip(),
        "temp": temp,
        "date": date.strip()
        }
    
    
    
def read_valid(lines: list[str]) -> list[dict]:
    '''
    Разбирает строки журнала, пропуская
    пустые и негодные
    '''
    pass

def average_by_city(records: list[dict]) -> dict:
    '''
    Средняя температура по каждому городу,
    округлённая до десятых
    '''
    pass

def warmest_city(records: list[dict]) -> str:
    '''
    Город с наибольшей средней температурой.
    При равенстве _ первый по алфавиту.
    '''
    pass