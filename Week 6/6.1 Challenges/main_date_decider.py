# reads file, returns dictionary, in the dictionary list of names is value and availability is a key
import csv


IN_FILEPATH = 'data_test.csv'

def read_csv_file(csv_path, delimiter):
    '''this method returns a list of rows that contains a list of columns given a path'''
    data_list = []
    csvfile = open(csv_path, encoding='utf-8-sig')
    for row in csv.reader(csvfile, delimiter=delimiter):
        data_list.append(row)
    return data_list


def build_availability_dictionary(csv_object: object) -> object:
    '''this method will return the dictionary where the key is the day of the week and the value is the list of people
    available that day'''
    availability_dictionary = {}
    for row_number,row in enumerate(csv_object):
        for column_number,column in enumerate(row):
            if row_number == 0:
                if column_number > 0:
                    availability_dictionary[column] = []
            else:
                if column == '1':
                    if column_number == 1:
                        availability_dictionary[csv_object[0][1]].append(row[0])
                    if column_number == 2:
                        availability_dictionary[csv_object[0][2]].append(row[0])
                    if column_number == 3:
                        availability_dictionary[csv_object[0][3]].append(row[0])
                    if column_number == 4:
                        availability_dictionary[csv_object[0][4]].append(row[0])
                    if column_number == 5:
                        availability_dictionary[csv_object[0][5]].append(row[0])
                    if column_number == 6:
                        availability_dictionary[csv_object[0][6]].append(row[0])
                    if column_number == 7:
                        availability_dictionary[csv_object[0][7]].append(row[0])
    return availability_dictionary


def return_availability(availability_dictionary):
    available_days = []
    for day in availability_dictionary.keys():
        if len(availability_dictionary[day]) == 3:
            available_days.append(day)
    return available_days


def main():
    print(return_availability(build_availability_dictionary(read_csv_file(IN_FILEPATH, ';'))))

if __name__ == "__main__":
    main()

# def compare_availability():
#
#
# def write_availability():
#