import logstats

def main():
    filename = input("Введите имя файла журнала: ").strip()
    
    total_lines = 0
    error_count = 0
    counts = {}
    
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines() 
    
    with open(filename, "r", encoding="utf-8") as f:
        counts = logstats.count_levels(f)
        
    total_lines = sum(counts.values())
    error_count = counts.get("ERROR", 0)
    broken_count = counts.get("BROKEN", 0)

    print(total_lines)
    print(error_count)
    print(broken_count)
    
    with open(filename, "r", encoding="utf-8") as f:
        top_errs = logstats.top_errors(f, n=3) 
        
    report_text = logstats.format_report(counts, top_errs)
    
    with open("report.txt", "w", encoding="utf-8") as f:
        f.write(report_text)

if __name__ == "__main__":
    main()