from os.path import exists


class SourceFile:
    @staticmethod
    def get_lines(file_path):
        if not exists(file_path):
            print("File not found.")
            return None

        with open(file_path, encoding='utf-8', mode='r') as file:
            for line in file.readlines():
                yield line
