def max_widths(list_of_dicts):
    widths = {key: len(str(key)) for key in list_of_dicts[0].keys()}

    for line in list_of_dicts:
        for key, value in line.items():
            if value and widths[key] < len(str(value)):
                widths[key] = len(str(value))

    return widths


def print_as_table(list_of_dicts):
    widths = max_widths(list_of_dicts)
    table_headers = list_of_dicts[0].keys()

    for header in table_headers:
        print(f"{header:>{widths[header]}}", end=" ")
    print()

    for row in list_of_dicts:
        for key, value in row.items():
            print(f"{value if value else '':>{widths[key]}}", end=" ")
        print()
