import csv
import os
import statistics

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
    with open(filename, 'r', encoding='utf-8') as fin:
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
    prices = []
    for pur in data:
        prices.append(pur.price)
    # Cool way - list comp or generator expression

    ave_price = statistics.mean(prices)
    print('The average home price is ${:,}'.format(int(ave_price)))

    # average price of 2 bedroom?
    prices = []
    for pur in data:
        if pur.beds == 2:
            prices.append(pur.price)
    ave_price = statistics.mean(prices)
    print('The average price of a 2-bedroom home is ${:,}'.format(int(ave_price)))


if __name__ == '__main__':
    main()
