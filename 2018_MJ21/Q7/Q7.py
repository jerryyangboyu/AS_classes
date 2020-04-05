from typing import List

Mark: List[int] = [10, 20, 60, 41, 54, 78, 98, 32, 12, 4]


def process_mark(mark: List[int]) -> int:
    total: int = 0
    position: int = 0
    highest: int = mark[0] if len(mark) != 0 else -float("INF")
    for i in mark:
        total += i
        if i > highest: highest, position = i, mark.index(i)
    print("The average is {0} and the highest is {1}".format(total / len(mark), highest))
    return position


if __name__ == '__main__':
    print(process_mark(Mark))
