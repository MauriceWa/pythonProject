def file_constructor(file_path):
    with open(file_path) as parsed_file:
        contents = parsed_file.read()
        return file_constructor(parsed_file)



def parse_json_file(parsed_file):
    saved_data = {}
    key = None
    value = ''
    is_it_a_value = False

    for line in parsed_file:
        if line == '"':
            is_it_a_value = not is_it_a_value
        elif line == ':' and not is_it_a_value:
            key = value.strip(' "')
            value = ''
        elif line == ',' and not is_it_a_value:
            saved_data[key] = value.strip(' "')
            value = ''
        else:
            value += line

        if key is not None:
            saved_data[key] = value.strip(' "')

        return saved_data
