from os.path import exists, isdir, isfile
from os import scandir


class SourceFile:
    @staticmethod
    def get_lines(file_path):
        if not exists(file_path):
            print("File not found.")
            return None

        with open(file_path, encoding='utf-8', mode='r') as file:
            for line in file.readlines():
                yield line


class SourceDirectory:
    @staticmethod
    def get_files(directory_path):
        for entry in scandir(directory_path):
            if entry.is_file():
                yield entry.path
            if entry.is_dir():
                yield from SourceDirectory.get_files(entry.path)


class SourceProject:
    @staticmethod
    def get_files(start_path):
        if not exists(start_path):
            print("File not found.")
            return None

        if isfile(start_path):
            yield start_path
        elif isdir(start_path):
            yield from SourceDirectory.get_files(start_path)

