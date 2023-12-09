import csv
import time


def file_cut_date_and_data(path: str, folder:str) -> None:
    """Open .csv file from path and fill "1/" folder with 2 files : DATA and DATE

    Args:
        path (str): path to file to cut
    """
    date = []
    data = []
    with open(path, "r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            date.append([row[0]])
            data.append([row[1]])
    with open(f"{folder}\\X.csv", "w", encoding="utf-8", newline="") as file_x:
        writer = csv.writer(file_x)
        writer.writerows(date)
    with open(f"{folder}\\Y.csv", "w", encoding="utf-8", newline="") as file_y:
        writer = csv.writer(file_y)
        writer.writerows(data)
    print("end")