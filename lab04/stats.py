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
    valid_records = []
    for line in lines:
        if not line.strip():
            continue
        try:
            record = parse_record(line)
    
            valid_records.append(record)
        except ValueError:
                continue
    return valid_records

def average_by_city(records: list[dict]) -> dict:
    '''
    Средняя температура по каждому городу,
    округлённая до десятых
    '''
    if not records:
        return {}
    total = {}
    count = {}

    for rec in records:
        city = rec['city']
        temp = rec['temp']
        total[city] = total.get(city, 0) + temp
        count[city] = count.get(city, 0) + 1
    averages = {}
    for city in total:
        avg = total[city]/count[city]
        averages[city] = round(avg, 1)
    return averages

def warmest_city(records: list[dict]) -> str:
    '''
    Город с наибольшей средней температурой.
    При равенстве _ первый по алфавиту.
    '''
    averages = average_by_city(records)
    if not averages:
        return ''
    best_city = min(averages.items(), key = lambda x: (-x[1], x[0]))[0]
    return best_city