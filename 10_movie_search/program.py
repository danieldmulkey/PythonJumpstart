import movie_svc
import requests.exceptions


def main():
    print_header()
    search_event_loop()


def print_header():
    print('-----------------------------')
    print('      MOVIE SEARCH APP')
    print('-----------------------------')
    print()


def search_event_loop():
    # Official:
    search = "ONCE_THROUGH_LOOP"
    while search.lower() != 'x':
        # Apparently, put try/except in event loop instead of movie_svc module? I guess it is more transparent as
        # to loop flow.
        try:
            search = input('Movie search text (x to exit): ')
            if search.lower() != 'x':
                results = movie_svc.find_movies(search)
                print('Found {} results'.format(len(results)))
                for r in results:
                    print('{} -- {}'.format(r.year, r.title))
                print()

        except requests.exceptions.ConnectionError:
            print("Error: Network appears to be down")
        except ValueError:
            print('Search text is required')
        except Exception as x:
            print("Unexpected error. Details: {}".format(x))

    # Why not this way?
    # while True:
    #     search = input('Movie search text (x to exit): ')
    #     if search.lower() == 'x':
    #         break
    #     results = movie_svc.find_movies(search)
    #     print('Found {} results'.format(len(results)))
    #     for r in results:
    #         print('{} -- {}'.format(r.year, r.title))
    #     print()

    print('Exiting...')


if __name__ == '__main__':
    main()
