# pcost.py
#
# Exercise 1.27

with open('Data/portfolio.csv', 'rt') as p:
    headers = next(p)
    total = 0
    for line in p:
        row = line.split(',')
        print(row)
        total = total + (int(row[1]) * float(row[2]))

print(f'Total cost {total}')
print()

# Exercise 1.28: Other kinds of “files”
# gzip

import gzip

with gzip.open('Data/portfolio.csv.gz', 'rt') as g:
    for line in g:
        print(line, end='')
print()

# Exercise 1.30
# Turning a script into a function

def portfolio_cost(filename):
    with open(filename, 'rt') as p:
        next(p)
        total = 0
        for line in p:
            row = line.split(',')
            print(row)
            total = total + (int(row[1]) * float(row[2]))

    print(f'Total cost {total}')
    print()

portfolio_cost('Data/portfolio.csv')

# Exercise 1.31
# Error handling

def portfolio_cost(filename):
    with open(filename, 'rt') as p:
        next(p)
        total = 0
        for line in p:
            row = line.split(',')
            try:
                total = total + (int(row[1]) * float(row[2]))
            except ValueError:
                print(f'Badly formatted line')

    print(f'Total cost {total}')
    print()

portfolio_cost('Data/missing.csv')

# Exercise 1.32
# Using a lib funciton -- csv module

import csv;

def portfolio_cost(filename):
    f = open(filename)
    rows=csv.reader(f)
    next(rows)
    total = 0
    for row in rows:
        try:
            total = total + (int(row[1]) * float(row[2]))
        except ValueError:
            print(f'Badly formatted line')

    print(f'Total cost {total}')
    print()

print('>>>>> Using CSV module')
print('Case #1')
portfolio_cost('Data/portfolio.csv')
print('Case #2')
portfolio_cost('Data/missing.csv')

# Exercise 1.33
# Reading from the command line

import sys;

def portfolio_cost(filename):
    f = open(filename)
    rows=csv.reader(f)
    next(rows)
    total = 0
    for row in rows:
        try:
            total = total + (int(row[1]) * float(row[2]))
            print(total)
        except ValueError:
            print(f'Badly formatted line')
    return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

print('>>>>> Reading from command line')
cost = portfolio_cost(filename);
print('Total cost: ', cost)