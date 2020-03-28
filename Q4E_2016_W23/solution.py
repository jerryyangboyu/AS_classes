from typing import *


class Solution:
    def __init__(self, p_code: List[str]):
        self.p_code = p_code

    def product_code_search(self, search_code: str) -> int:
        for i in self.p_code:
            if search_code == i:
                return self.p_code.index(i)
        return -1


if __name__ == '__main__':
    p_codes: List[str] = ["0198", "0202", "0376", "0014"]
    solution: Solution = Solution(p_codes)
    user_search_code: str = input("Enter the product code to search:")
    result: int = solution.product_code_search(user_search_code)
    print("The search result is: {0}".format(result))
