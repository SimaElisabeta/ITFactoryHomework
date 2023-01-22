import csv
import json


def replace_char_in_file_CSV(file_name, find, replace):
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        data = list(reader)
    with open(file_name, "w") as f:
        for i in range(len(data)):
            for j in range(len(data[i])):
                if find in data[i][j]:
                    data[i][j] = data[i][j].replace(find, replace)
        writer = csv.writer(f, lineterminator="\n")
        writer.writerows(data)


replace_char_in_file_CSV("username.csv", "a", "")


def replace_char_in_file_JSON(file_name, find, replace):
    with open(file_name, "r") as f:
        data = json.load(f)
    with open(file_name, "w") as f:
        for i in range(len(data)):
            for key, value in data[i].items():
                if find in value:
                    data[i].update({key: value.replace(find, replace)})
        json.dump(data, f, indent=4)


replace_char_in_file_JSON("username.json", "a", "")
