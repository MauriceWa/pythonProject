hero_list = []
villain_list = []
def read_file(file_name):
    with open(file_name, "r") as file:
        list = []
        for index, line in enumerate(file):
            if index > 0:
                line_list = line.split(";")
                dict = {
                    "naam": line_list[0],
                    "kracht": line_list[1],
                    "verdediging": line_list[2],
                    "aanvallen": line_list[3],
                    "beschrijving": line_list[4]
                }
                list.append(dict)
    return list




def main():
    hero_list = read_file("helden.txt")
    villain_list = read_file("vijanden.txt")
    for hero in hero_list:
        print(hero)
    for villain in villain_list:
        print(villain)


if __name__ == '__main__':
    main()