import json
import csv


def split_in_half_JSON_file(file_name, first_file, second_file):
    with open(file_name, "r") as f:
        data = json.load(f)
        first_half = data[:(len(data) // 2)]
        second_half = data[(len(data) // 2):]
    with open(first_file, "w") as f:
        json.dump(first_half, f, indent=4)
    with open(second_file, "w") as f:
        json.dump(second_half, f, indent=4)


split_in_half_JSON_file("username.json", "username_first_half.json", "username_second_half.json")


def split_in_half_CSV_file(file_name, first_file, second_file, use_header):
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        data = list(reader)
        header = data[0]
        first_half = data[0:((len(data) + 1) // 2)] if use_header else data[:(len(data) // 2)]
        second_half = header + data[((len(data) + 1) // 2):] if use_header else data[(len(data) // 2):]
    with open(first_file, "w", ) as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerows(first_half)
    with open(second_file, "w") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerows(second_half)


split_in_half_CSV_file("username.csv", "username_first_half.csv", "username_second_half.csv", True)
