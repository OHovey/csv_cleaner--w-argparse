from csv_cleaner import CsvClean
import sys
import os

if __name__ == '__main__':
    if len(sys.argv) < 2:
        c = CsvClean()
    elif len(sys.argv) < 3 and '.csv' not in sys.argv[1] or len(sys.argv) < 3 and 'xlsx' not in sys.argv[1]:
        c = CsvClean(sys.argv[1])
    elif len(sys.argv) < 3 and '.csv' in sys.argv[1] or len(sys.argv) < 3 and '.xlsx' in sys.argv[1]:
        c = CsvClean(file = sys.argv[2])
    else:
        c = CsvClean(sys.argv[1], sys.argv[2])
    
    c.clean()
