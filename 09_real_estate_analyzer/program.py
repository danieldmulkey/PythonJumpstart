import csv
import os

try:  # one way to work on Py2 and Py3 simultaneously
    import statistics
except:
    # error code instead
    import statistics_standin_for_py2 as statistics

from data_types import Purchase


def main():
    print_header()

    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


def print_header():
    print('------------------------------')
    print(' REAL ESTATE DATA MINING APP')
    print('------------------------------')
    print()


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data',
                        'SacramentoRealEstateTransactions2008.csv')


def load_file(filename):
    # with open(filename, 'r', encoding='utf-8') as fin:
    with open(filename, 'r') as fin:  # for pre-statistics module
        # DictReader is fantastic for CSVs
        reader = csv.DictReader(fin)  # assumes first line is header naming columns
        purchases = []
        for row in reader:  # each row is an (OrderedDict) dict now
            p = Purchase.create_from_dict(row)  # pass in a dict
            purchases.append(p)

        return purchases

        # header = fin.readline().strip()  # to take off \n
        # reader = csv.reader(fin)
        # for row in reader:
        #     print(type(row), row)


# def load_file_basic(filename):
#     with open(filename, 'r', encoding='utf-8') as fin:
#         header = fin.readline().strip()  # to take off \n
#         print('Found header: ' + header)
#
#         lines = []
#         for line in fin:
#             line_data = line.strip().split(',')  # bad for edge cases
#             bed_count = line_data[4]
#             lines.append(line_data)
#
#         print(lines[:5])

# def get_price(p):
#     return p.price


def query_data(data):  # : list[Purchase]):  # can specify data type of arg
    # Apparently, can specify data type within arg in docstring, but not as type hint for PyCharm.

    # if data was sorted by price
    # Lame: write a function just to sort this:
    # data.sort(key=get_price)  # supply method object on which to sort data objects of list
    # Cool: lambda fcts (inline method:
    data.sort(key=lambda p: p.price)
    # lambda arg: return

    # most expensive?
    high_purchase = data[-1]
    print('The most expensive house is ${:,} with {} beds and {} baths'.format(high_purchase.price, high_purchase.beds,
                                                                               high_purchase.baths))

    # least expensive?
    low_purchase = data[0]
    print('The least expensive house is ${:,} with {} beds and {} baths'.format(low_purchase.price, low_purchase.beds,
                                                                                low_purchase.baths))

    # average price?
    # Lame way - loop through
    # prices = []
    # for pur in data:
    #     prices.append(pur.price)
    # Cool way - list comp or generator expression

    prices = [
        p.price  # projection or items
        for p in data  # the set to process
    ]

    ave_price = statistics.mean(prices)
    print('The average home price is ${:,}'.format(int(ave_price)))

    # Procedural:
    # average price of 2 bedroom?
    # prices = []
    # for pur in data:
    #     if pur.beds == 2:
    #         prices.append(pur.price)

    # List comprehension:
    # two_bed_homes = [
    #     p  # projection or items
    #     for p in data  # the set to process
    #     if p.beds == 2  # test / condition
    # ]

    # Generator expression!:
    two_bed_homes = (
        p  # projection or items
        for p in data  # the set to process
        if announce(p, '2-bedrooms, found {}'.format(p.beds)) and p.beds == 2  # test / condition
    )

    homes = []  # list because access repeatedly
    for h in two_bed_homes:
        if len(homes) >= 5:
            break
        homes.append(h)

    # If homes was a gen exp, it would be consumed on first use
    ave_price = statistics.mean((announce(p.price, 'price') for p in homes))  # gen exp because throw away
    ave_baths = statistics.mean((p.baths for p in homes))
    ave_sq_ft = statistics.mean((p.sq_ft for p in homes))
    print('The average 2-bedroom home is ${:,}, baths={}, sq_ft={:,}'
          .format(int(ave_price), round(ave_baths, 1), round(ave_sq_ft, 1)))


def announce(item, msg):
    print('Pulling item {} for {}'.format(item, msg))
    return item


if __name__ == '__main__':
    main()
