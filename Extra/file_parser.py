def file_constructor(file_path):
    with open(file_path) as parsed_file:
        contents = parsed_file.read()
        return file_constructor(parsed_file)



def parse_json_file(parsed_file):
    saved_data = {}
    