import journal


# from journal import load, save  # sometimes ok
# from journal import *  # no!

def main():
    print_header()
    run_event_loop()


def print_header():
    print('-----------------------')
    print('      JOURNAL APP')
    print('-----------------------')


def run_event_loop():
    print('What do you want to do with your journal?')
    cmd = 'EMPTY'
    journal_name = 'default'
    journal_data = journal.load(journal_name)  # []  # list()

    while cmd != 'x' and cmd:  # because empty string evaluates to False
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()
        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x' and cmd:  # so empty command doesn't trigger
            print("Sorry, we don't understand {}".format(cmd))

    print('Done, goodbye.')
    journal.save(journal_name, journal_data)


def list_entries(data):
    print('Your journal entries:')
    entries = reversed(data)
    for (idx, entry) in enumerate(entries):
        print('* [{}] {}'.format(idx + 1, entry))


def add_entry(data):
    text = input('Type your entry, <enter> to exit: ')
    journal.add_entry(text, data)


# __file__ is current filepath
# __name__ changes if not target of execution
if __name__ == '__main__':
    main()
