# report.py
#
# Reference: Exercise 1.30
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

# portfolio_cost('Data/portfolio.csv')    


# Exercise 2.4
import csv;

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows= csv.reader(f)
        next(rows)

        for row in rows:
            t=(row[0], int(row[1]), float(row[2]))
            portfolio.append(t)
        print(portfolio)
        return portfolio

# Exercise 2.5
# Use dicts instead of tuples
import csv;

def read_portfolio_dict(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows= csv.reader(f)
        next(rows)

        for row in rows:
            o = {
                "name": row[0],
                "price": float(row[2]),
                "shares": int(row[1])
            }
            portfolio.append(o)
        # print(portfolio)
        return portfolio
    
# Exercise 2.6
# Use containers instead of tuples/dicts
import csv

def read_prices(filename):
    with open(filename, 'rt') as p:
        rows = csv.reader(p)

        portfolio = {}

        for row in rows:
            if len(row) > 0:
                portfolio[row[0]] = float(row[1])

        return portfolio

# Exercise 2.7
# Combine everything

def can_i_retire():
    shares = read_portfolio_dict('Data/portfolio.csv')
    prices = read_prices('Data/prices.csv')

    total = 0
    pnl = 0

    for entry in shares:
        key = entry['name']
        print(entry, key)
        total += entry['shares']*prices[key]
        pnl += (entry['price'] - prices[key]) * entry['shares']

    return {'total': round(total, 2), 'pnl': round(pnl, 2)}