class FileReader:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode, encoding='UTF-8')
        return self.file

    def __exit__(self, _type, msg, traceback):
        if _type:
            print(msg)
        self.file.close()
        return False


with FileReader('Books.txt', 'w') as file:
    file.write("asdf\n")
    file.write("asdf\n")

with FileReader('Books.txt', 'r') as file:
    for line in file:
        print(line)
