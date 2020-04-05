class FileHandler:
    def __init__(self, filename: str, mode: str):
        self.filename: str = filename
        self.mode: str = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode, encoding='UTF-8')
        return self.file

    def __exit__(self, _type, msg, traceback):
        if _type:
            print(msg)
        self.file.close()
        return False
