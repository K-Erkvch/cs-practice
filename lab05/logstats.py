from collections import Counter

def parse_event(line: str) -> dict:
    line = line.strip()
    parts = line.split(' ', maxsplit=2)
    
    if len(parts) < 3:
        raise ValueError("Недостаточно частей в строке")
        
    time_str, level, message = parts
    valid_levels = {"DEBUG", "INFO", "WARNING", "ERROR"}
    
    if level not in valid_levels:
        raise ValueError(f"Неизвестный уровень лога: {level}")
        
    return {
        "time": time_str,
        "level": level,
        "message": message
    }

def count_levels(lines: list[str]) -> dict:
    counts = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
            level = event["level"]
            counts[level] = counts.get(level, 0) + 1
        except ValueError:
            counts["BROKEN"] = counts.get("BROKEN", 0) + 1
            
    return counts

def top_errors(lines: list[str], n: int) -> list[list]:
    errors = []
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
            if event["level"] == "ERROR":
                errors.append(event["message"])
        except ValueError:
            pass

    counter = Counter(errors)
    
    
    sorted_errors = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
    
    result = [[msg, count] for msg, count in sorted_errors[:n]]
    return result

def format_report(counts: dict, errors: list[list]) -> str:
    report_lines = ["Отчёт по журналу", ""]
    
    for level in sorted(counts.keys()):
        report_lines.append(f"{level}: {counts[level]}")
        
    report_lines.append("")
    report_lines.append("Частые ошибки:")
    
    for err_msg, count in errors:
        report_lines.append(f"— {err_msg} — {count}")
        
    return "\n".join(report_lines) + "\n"