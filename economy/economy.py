currency = input("Which currency? ")
currency = currency + '.txt'

with open(currency) as file:
    for i, line in enumerate(file):
        print(i)

#value = (gdp/supply) * avg_price
#conversion = value1 / value2