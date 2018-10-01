import pandas as pd 
import os
import shutil
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

    @classmethod
    def create_empty(cls):
        return cls()


    @classmethod
    def create_with_file(cls, file):
        return cls(file=file)

    
    @classmethod
    def create_with_path(cls, path):
        return cls(path=path)

    @classmethod
    def create_with_file_and_filename(cls, file, new_filename):
        return cls(file=file, filename=filename)


    @classmethod
    def create_with_file_and_path(cls, path, file):
        return cls(path, file)


    @classmethod
    def create_with_all(cls, path, file, new_filename):
        return cls(path, file, filename)

    @staticmethod
    def _get_files(path):
        return [c for c in os.listdir(path) if '.csv' in str(c) or '.xlsx' in str(c)]


    def __init__(self, path=os.getcwd(), file=None, new_filename=None):
        
        if path[-1] != '/':
            self.path = '{}/'.format(path)
        else:
            self.path = path
        
        self.file = file
        self.new_filename = new_filename
        
        if self.file is None:
            self.files = self._get_files(self.path)
            self.file = False
        elif file is not type(list) and self.new_filename is None: 
            self.new_filename = 'new_{}'.format(self.file)

        if self.path != os.getcwd() and self.file != False:
            shutil.copy('{}{}'.format(self.path, self.file), os.getcwd())


    def __del__(self):
        os.remove(self.file)


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
                self._file_writer(file)



           
