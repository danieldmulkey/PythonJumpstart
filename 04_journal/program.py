def print_header():
    print('-------------------------------')
    print('     PERSONAL JOURNAL APP')
    print('-------------------------------')


def count_newlines(file):
    pass


def load_journal():
    journal_file = ''
    print('... loading data from {} ...'.format(journal_file))
    file = open(journal_file)
    num_entries = count_newlines(file)
    print('... loaded {} entries ...'.format(num_entries))
    return file


def query_user(jrn_file):
    pass


def process_choice(choice, jrn):
    pass


def build_example_journal():
    pass


def main():
    print_header()
    jrn = load_journal()
    while True:
        choice = query_user(jrn)
        process_choice(choice, jrn)
    save_journal(jrn)


# if __name__ == '__main__':
# I could go through and come up with a solution, but I'm just going to follow along with the video as my method
# would demonstrate a fair amount of bad style.
