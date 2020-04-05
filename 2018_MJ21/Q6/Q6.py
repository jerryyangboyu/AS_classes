from typing import List


def pixels3():
    pic: List[List[int]] = [[240, 80], [10, 240]]
    temp: List[List[float]] = [[1.1 * j for j in i] for i in pic]
    return [[burnout := True for j in i if j >= 255] for i in temp] and temp


if __name__ == '__main__':
    print(pixels3())
