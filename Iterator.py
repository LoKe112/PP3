import os
import csv
import time


class Iterator:

    def __init__(self, name_of_file: str) -> None:
        """Initialization

        Args:
            name_of_file (str): _description_
        """
        self.name_of_file = name_of_file
        self.counter = 0
        self.list = []
        file = open(self.name_of_file, "r", encoding='utf-8')
        for row in file:
            self.list.append(row)
        file.close

    def __iter__(self):
        return self

    def __next__(self) -> int:
        """next

        Raises:
            StopIteration: _description_

        Returns:
            int: _description_
        """
        if self.counter < len(self.list):
            tmp = self.list[self.counter]
            self.counter += 1
            return tmp
        else:
            raise StopIteration
    
def next_iter(path: str) -> tuple:
    """get next date in file

    Args:
        path (str): path to dataset.csv 

    Returns:
        tuple: ((date, we find), (data, we found))

    Yields:
        Iterator[tuple]: ((date, we find), (data, we found))
    """
    with open(path, "r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            data = row[0]
            mass = []
            for i in range(1, len(row)):
                mass.append(row[i])
            yield (data, mass)
            

iter = next_iter("dataset.csv")
first = next(iter)
print(first)
second = next(iter)
print(second)

iter = Iterator("dataset.csv")

for i in range(1,10):
    print(next(iter))