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
    for m in matches:
        match_count += 1
        print(m)
        # print('------- MATCH --------')
        # print('file: ' + m.file)
        # print('line: {}'.format(m.line))
        # print('match: ' + m.text.strip())
        # print()

    print('Found {:,} matches.'.format(match_count))


def print_header():
    print('--------------------------------')
    print('         FILE SEARCH APP')
    print('--------------------------------')


def get_folder_from_user():
    folder = input('What folder would you like to search? ')
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_search_text_from_user():
    text = input('What text are we searching for [single phrases only] ')
    return text.lower()


def search_file(filename, search_text):
    # matches = []
    with open(filename, 'r', encoding='utf-8') as fin:

        line_num = 0
        for line in fin:
            line_num += 1
            if line.lower().find(search_text) >= 0:
                m = SearchResults(file=filename, line=line_num, text=line)
                yield m

                # return matches


def search_folders(folder, text):
    # all_matches = []
    items = os.listdir(folder)

    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            # matches = search_folders(full_item, text)
            # all_matches.extend(matches)  # list version

            # for m in matches:  # generator version
            #     yield m

            # yield from matches  # efficient generator version (Py 3.3+)
            yield from search_folders(full_item, text)  # better yet, don't store matches

        else:
            # matches = search_file(full_item, text)
            # extend() can append multiple items
            # all_matches.extend(matches)

            yield from search_file(full_item, text)

    # return all_matches


if __name__ == '__main__':
    main()
