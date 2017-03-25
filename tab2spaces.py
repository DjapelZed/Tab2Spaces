import os
import re
import argparse


COUNT_OF_SPACES = 4


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', help='Enter a path to file')
    parser.add_argument('-c', '--count', help='Enter a count of spaces')
    arguments = parser.parse_args()
    return arguments


def get_the_data(path):
    with open(path, 'r') as file:
        data = file.read()
    return data


def tab2spaces(data, count_of_spaces): # By default COUNT_OF_SPACES = 4
    new_data = re.sub(r'\t', u' ' * count_of_spaces, data)
    return new_data


def write_the_new_data(new_data, path):
    with open(path, 'w') as file:
        file.write(new_data)


if __name__ == '__main__':
    arguments = get_arguments()
    if not arguments.path:
        file_path = input('Enter a path to the file: ')
    else:
        file_path = arguments.path
    if os.path.isfile(file_path):
        if arguments.count:
            new_COUNT_OF_SPACES = int(arguments.count)
        else:
            new_COUNT_OF_SPACES = int(input('Enter a count of spaces: '))
        data = get_the_data(file_path)

        try:
            new_data = tab2spaces(data, new_COUNT_OF_SPACES)
        except ValueError as error:
            new_data = tab2spaces(data, COUNT_OF_SPACES)

        write_the_new_data(new_data, file_path)
        print('Completed!')
    else:
        print('Incorrect path!')
        exit()