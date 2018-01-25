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
    while True:
        try:
            search = input('Movie search text (x to exit): ')
            if search.lower() == 'x':
                break

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

    print('Exiting...')


if __name__ == '__main__':
    main()
