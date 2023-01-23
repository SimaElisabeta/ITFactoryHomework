import copy
import csv


def remove_element_in_CSV_file(file_name, check_char):
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    with open(file_name, 'w', newline='') as f:
        new_data = []
        for line in data:
            current_list = []
            for element in line:
                if check_char not in element:
                    current_list.append(element)
            new_data.append(current_list)
        writer = csv.writer(f)
        writer.writerows(new_data)


remove_element_in_CSV_file("username.csv", "a")


def remove_element_in_CSV_file_2(file_name, char):
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    with open('edit_2_' + file_name, 'w', newline='') as f:
        copy_data = copy.deepcopy(data)
        for i in range(len(data)):
            for word in data[i]:
                if char in word:
                    copy_data[i].remove(word)
        writer = csv.writer(f)
        writer.writerows(copy_data)


remove_element_in_CSV_file_2("username.csv", "a")
