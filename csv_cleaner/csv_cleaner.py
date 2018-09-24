import pandas as pd 
import os
import argparse

class CsvClean:
    """A module for quickly removing empty rows from csv files

    Args:
        path (optional): path where the target file(s) is located.
        if no argument is given, the current working directory will be used.

        filename (optional): the csv file to be modified and copied.
                            If no argument is given, all files with the '.csv'
                            or '.xlsx' suffix will be used.

    Returns:
        ...

    """


    def __init__(self, path=None, file=None, new_filename=None):

        if path is not None:
            self.path = path
        else:
            self.path = os.getcwd()
        self.path += '/'

        if file is not None:
            self.file = file
        else:
            self.files = [c for c in os.listdir(path) if '.csv' in str(c) or '.xlsx' in str(c)]
            self.file = False

        if new_filename is not None:
            self.new_filename = new_filename
        elif file is not None and new_filename is None: 
            self.new_filename = 'new_{}'.format(self.file)


    def _file_writer(self, file):

        if '~$' in str(file):
            file = file.replace('~$', '')

        try:
            full_path = "{}{}".format(self.path, file)
        except NotADirectoryError:
            raise NotADirectoryError('could not locate file: {} at {}\n Full path at: {}'.format(self.file, self.path, full_path))
            
        if '.xlsx' in str(full_path):
            try:
                df = pd.read_excel(full_path)
                df = df.dropna(how='all')
                df.to_csv(self.new_filename.replace('.xlsx', '.csv'), encoding='utf-8', index=False)
            except:
                pass
            return 

        df = pd.read_csv(full_path)
        df = df.dropna(how='all')
        df.to_csv(self.new_filename)
        return
        
    
    def clean(self):

        if self.file:
            self._file_writer(self.file)
        else:
            for file in self.files:
                self.new_filename = '{}{}'.format('new_', file)
                print(file)
                self._file_writer(file)


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
        c = CsvClean(path, file, output)   
    elif args.path and args.file:
        path = args.path
        file = args.file
        c = CsvClean(path, file)
    elif args.path:
        path = args.path
        c = CsvClean(path)
    elif args.file and args.output:
        file = args.file
        output = args.output
        c = CsvClean(file=file, new_filename=output)
    elif args.file:
        file = args.file
        c = CsvClean(file = file)
    
    c.clean()
           
