def clean_string(string):
    string = string.replace('\r', '').replace('\n', '')
    while string[0] == ' ':
        string = string[1: ]
    while string[-1] == ' ':
        string = string[: -1]
    return string


