import os
import collections

SearchResults = collections.namedtuple('SearchResult',
                                       'file, line, text')


def main():
    print_header()

    folder = get_folder_from_user()
    if not folder:
        print("Sorry, can't search that location.")
        return

    text = get_search_text_from_user()
    if not text:
        print("We can't search for an empty string")
        return

    matches = search_folders(folder, text)

    match_count = 0
    for _ in matches:
        match_count += 1

    print('Found {:,} matches.'.format(match_count))


def print_header():
    print('--------------------------------')
    print('        FILE SEARCH APP')
    print('--------------------------------')


def get_folder_from_user():
    folder = input('What folder would you like to search? ')
    if folder == 'default':
        return r'C:\Users\Daniel\Documents\PycharmProjects\PythonJumpstart\08_file_searcher\test_set'

    if not folder or not folder.strip():  # strip in case folder is whitespace?
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_search_text_from_user():
    text = input('What text are we searching for [single phrases only] ')
    return text.lower()


def search_folders(folder, text):
    items = os.listdir(folder)

    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            yield from search_folders(full_item, text)  # better yet, don't store matches

        else:
            yield from search_file(full_item, text)


def search_file(filename, search_text):
    with open(filename, 'r', encoding='utf-8') as fin:
        line_num = 0

        for line in fin:
            line_num += 1
            if line.lower().find(search_text) >= 0:
                m = SearchResults(file=filename, line=line_num, text=line)
                yield m


if __name__ == '__main__':
    main()
