# reads file, returns dictionary, in the dictionary each name is key and availability is a list of values
in_filepath = 'data_decider.txt'

def read_file():
    res =[]
    with open(in_filepath) as file:
        for line in file:
            person, day = line.split()

            when = {}
            when['person'] = person
            when['day'] = day
            res.append(when)
        return res





def main():
     data = read_file()
     print(data)

     if __name__ == "__main__":
         main()
# def compare_availability():
#
#
# def write_availability():
#