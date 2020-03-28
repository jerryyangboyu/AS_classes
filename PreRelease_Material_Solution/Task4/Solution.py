from typing import *
from FileHandler import FileHandler


class Solution:
    @staticmethod
    def parse_title(one_line: str):
        return one_line.split('#')[0]

    @staticmethod
    def validate_length(prompt: str, err_message: str, length: int) -> str:
        res: str = input(prompt)
        while len(res) != length:
            print(err_message)
            res = input(prompt)
        return res

    @staticmethod
    def valid_range(prompt: str, err_message: str, length: int) -> int:
        res: int = int(input(prompt))
        while res <= length:
            print(err_message)
            res = int(input(prompt))
        return res

    def __init__(self):
        with FileHandler('BooksRecord.txt', 'r') as oldFile:
            for line in oldFile:
                print("Updating details for bool: {0}".format(self.parse_title(line)))
                with FileHandler('UpdatedBooksRecord.txt', 'a') as newFile:
                    isbn: str = self.validate_length("Please enter isbn number: ", "ISBN should consist of 11 digit",
                                                     11)
                    date_published: str = self.validate_length("Please enter the date published: ", "Date published "
                                                                                                    "should has 8 "
                                                                                                    "digit!", 8)
                    num_copies_str: int = self.valid_range("Please enter number of copies: ", "Number of copies shoud "
                                                                                              "be larger than one", 0)
                    newFile.write("{0}{1}#{2}#{3}#".format(line, isbn, date_published, num_copies_str))


if __name__ == '__main__':
    Solution()
