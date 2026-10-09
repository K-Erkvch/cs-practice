from stats import read_valid, average_by_city, warmest_city
import sys
def main():
    lines = sys.stdin.read().splitlines()
    valid_records = read_valid(lines)
    total_lines = len(lines)
    valid_count = len(valid_records)
    skipped_count = total_lines - valid_count
    print(valid_count)
    print(skipped_count)
    best_city = warmest_city(valid_records)
    if best_city:
        avg_temp = average_by_city(valid_records)[best_city]
        print(f'{avg_temp:.1f}')
    else:
        print('0.0')
if __name__ == '__main__':
    main()