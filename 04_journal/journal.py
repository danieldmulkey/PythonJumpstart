"""
This is the journal module.
"""
import os


def load(name):
    """
    This method creates and loads a new journal.
    
    :param name: The base name of the journal to load. 
    :return:  A new journal data structure populated with file data.
    """
    data = []
    filename = get_full_path_name(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())
    return data


def save(name, journal_data):
    filename = get_full_path_name(name)
    print('... saving to to {}'.format(filename))

    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')


def get_full_path_name(name):
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))
    return filename


def add_entry(text, journal_data):
    journal_data.append(text)