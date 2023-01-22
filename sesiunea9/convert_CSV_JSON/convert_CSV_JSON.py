import csv
import json


def convert_CSV_to_JSON(read_file_name, write_file_name):
    with open(read_file_name, "r") as f:
        reader = csv.DictReader(f)
        data = list(reader)
    with open(write_file_name, "w") as f:
        json.dump(data, f, indent=4)


convert_CSV_to_JSON('username.csv', 'username.json')


def convert_JSON_to_CSV(read_file_name, write_file_name):
    with open(read_file_name, "r") as f:
        data = json.load(f)
    with open(write_file_name, "w") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(data)


convert_JSON_to_CSV("color_palettes.json", "color_palettes.csv")
