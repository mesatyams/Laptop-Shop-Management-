import re
import json

STOCK_PATTERN = "(\S+\s?\S+\s?\S+\s?\S+\s?\S+|\S+\s?|\d+)"

class Read():
    def __init__(self):
        print('Reading Module Initialized!')
        self.stockFile = "data/laptop.txt"

    def readStock(self):
        b = open(self.stockFile)
        self.stock_data = json.load(b)  #read and strip down line breaks, store lines in an array
        b.close()
        return self.stock_data

    def stockList(self):
        stock = list(self.readStock())
        return stock