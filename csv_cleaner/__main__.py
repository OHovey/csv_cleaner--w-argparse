import argparse
from csv_cleaner import CsvClean

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""A script that allows you to remove empty rows from
                                                    csv or xlsx files by""")
    parser.add_argument('-path', help="Optional. The destination path of the file(s) to be processed", dest="path", 
                        type=str, required=False)
    parser.add_argument('-file', help="The name of the file to be processed", dest="file", type=str, required=False)
    parser.add_argument('-out', help="Optional. disired output name given to the new output file", dest="output", type=str, required=False)
    args = parser.parse_args()
    if args.path and args.file and args.output:
        path = args.path
        file = args.file
        output = args.output
        c = CsvClean.create_with_all(path, file, output)   
    elif args.path and args.file:
        path = args.path
        file = args.file
        c = CsvClean.create_with_file_and_path(path, file)
    elif args.path:
        path = args.path
        c = CsvClean.create_with_path(path)
    elif args.file and args.output:
        file = args.file
        output = args.output
        c = CsvClean.create_with_file_and_filename(file, output)
    elif args.file:
        file = args.file
        c = CsvClean.create_with_file(file)
    else:
        c = CsvClean.create_empty()

    print(c.file, c.path, c.new_filename)
    
    c.clean()