from typing import List, Tuple
from FileHandler import FileHandler


class Solution:
    @staticmethod
    def parse_line(single_line: str) -> Tuple[str, str]:
        res: List[str] = single_line.split("#")
        return res[0], res[1]

    @staticmethod
    def add_new_book(_title: str, _author: str):
        with FileHandler('Books.txt', 'a') as file:
            file.write("{0}#{1}#\n".format(_title, _author))
        # f can be passed as pointer reference to IO instance to increase efficiency
        # f.close() only when f is no longer used

    def search_book(self, author_to_found: str):
        found: bool = False
        _title: str = ""
        _author: str = ""

        with FileHandler('Books.txt', 'r') as file:
            for line in file:
                _title, _author = self.parse_line(line)

                if author_to_found == _author:
                    print("The book found is: {0}".format(_title))
                    found = True

        if not found:
            print("Book not found")


def unit_test_parse():
    _solution = Solution()
    _author, _book = _solution.parse_line("Jerry#Node JS#")
    print(_author, _book)


if __name__ == '__main__':
    solution: Solution = Solution()
    choice: str = ""
    title: str = ""
    author: str = ""

    while choice != 'n':
        print("************** MENU**************")
        print("*   1. Add a new book            *")
        print("*   2. Search a book by Author   *")
        print("*   3. Press n to quit           *")
        print("**********************************")

        choice = input("Enter your choice: ")
        if choice == '1':
            while len(title) <= 0 or len(title) >= 30:
                title = input("Input title:")
            while len(author) <= 0 or len(author) >= 20:
                author = input("Input author:")
            solution.add_new_book(title, author)
            title, author = "", ""

        elif choice == '2':
            solution.search_book(input("Input the author you want to search: "))

        elif choice == 'n':
            print("The program has existed successfully!")

        else:
            print("Invalid choice!")
