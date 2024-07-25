import datetime as dt                                               #library from python api
from Writting import Write
from Reading import Read

SHOW_TABLE_FORMAT = "{:<8} {:<25} {:<20} {:<20} {:<15} {:>10} {:>12}"

reader = Read()

writer = Write()

#############################################################################################
#           A Utility Class for Selling an item                                             #
#############################################################################################

class Stock():
    def __init__(self, dt):
        print('Stock Module Initialized!')
        self.dt = dt
        self.stock = reader.readStock()
        self.stockList = reader.stockList()
        self.billAmount = 0

    def showStock(self):
        print("---------------------- Here is the list of laptops ----------------------.  \n")
        print(SHOW_TABLE_FORMAT.format('S.No.', 'Company', 'Name', 'CPU', 'GPU', 'Price', 'Quantity'))
        print("-"*130)
        #prints the stock available to the screen
        for item in self.stockList:
            print(SHOW_TABLE_FORMAT.format(item['s.n'], item['company_name'], item['item_name'], item['cpu'], item['gpu'], item['price'], item['quantity']))
        print("-"*130)

    def sell(self):
        name = input("Enter your Customer Name: ")                  #taking first name as input from user
        phonenumber = input("Enter your Customer Phone Number: ")   #taking second name as input from user
        current_date = self.dt.getCurrentDate()
        current_time = self.dt.getCurrentTime()
        sellRecord = f"data/Bills/{name}_{current_date}.txt"        #locating sell record text file
        writer.setPath(sellRecord)
        writer.writeBill({
            "customer_name": name,
            "phone_number": phonenumber,
            "current_date": current_date,
            "current_time": current_time
        })
        item_count = 1
        while True:
            self.showStock()
            print("\n")
            try:
                index = int(input("Please input Item ID number: ")) - 1
                print(f'index {index + 1} selected!')
                try:                                                #can throw index out of bounds exception
                    if int(self.stockList[index]['quantity']) > 0:
                        print("Laptop is available.Thank you for selling")

                        quantity = int(input("please provide the number of quantity you want to buy: "))

                        price = int(self.stockList[index]['price'].replace('$', ''))

                        amount = quantity * price

                        writer.addItem({
                            "count": item_count,
                            "company_name": self.stockList[index]['company_name'],
                            "item_name": self.stockList[index]['item_name'],
                            "cpu": self.stockList[index]['cpu'],
                            "gpu": self.stockList[index]['gpu'],
                            "price": price,
                            "quantity": quantity,
                        })

                        self.billAmount += amount

                        self.stockList[index]['quantity'] = int(self.stockList[index]['quantity']) - quantity

                        writer.updateStock(self.stockList)

                        print('Bill Amount up till is : $' + str(self.billAmount))

                        yn = input("Do you want to sell more items?(press 'y' for 'yes' or any key for 'no'): ")
                        if yn.lower() != "y":
                            break                                   #end loop
                        item_count += 1
                    else:
                        print("laptop is not available in stock")
                        self.sell()
                except IndexError:
                    print("Please choose laptop as per their number.")
            except ValueError as err:
                print("Please choose as suggested.")
                print(err)
        # item_count = 2
        writer.finalBill({
            "total_amount": self.billAmount,
            "total_items": item_count,
            "route": "Kathmandu - Delhi",
            "shipping": 500
        })

    def buy(self):
        vender = input("Enter your Vender's Name: ")                  #taking first name as input from user
        phonenumber = input("Enter your Vender's Phone Number: ")   #taking second name as input from user
        current_date = self.dt.getCurrentDate()
        current_time = self.dt.getCurrentTime()
        buyRecord = f"data/Buys/{vender}_{current_date}.txt"        #locating sell record text file
        writer.setPath(buyRecord)
        writer.writeBuy({
            "vender_name": vender,
            "phone_number": phonenumber,
            "current_date": current_date,
            "current_time": current_time
        })
        self.billAmount = 0
        item_count = 1
        while True:
            company_name = input("Enter the Brand of the item: ")
            item_name = input("Enter the Item Name: ")
            cpu = input("Enter CPU Spec: ")
            gpu = input("Enter GPU Spec: ")
            price = float(input("Enter price (rate): "))
            quantity = int(input("Enter quantity: "))
            s_n = len(self.stockList) + 1
            self.billAmount += price * quantity
            new_item = {
                "s.n": s_n,
                "company_name": company_name,
                "item_name": item_name,
                "cpu": cpu,
                "gpu": gpu,
                "price": price,
                "quantity": quantity
            }
            writer.addItem({
                            "count": item_count,
                            "company_name": company_name,
                            "item_name": item_name,
                            "cpu": cpu,
                            "gpu": gpu,
                            "price": price,
                            "quantity": quantity,
                        })
            self.stockList.append(new_item)
            yn = input("Do you want to buy more items?(press 'y' for 'yes' or any key for 'no'): ")
            if yn.lower() != "y":
                break                                   #end loop
            item_count += 1
        writer.updateStock(self.stockList)
        writer.finalBill({
            "total_amount": self.billAmount,
            "total_items": item_count,
            "route": "Delhi - Kathmandu",
            "shipping": 15000
        })

#############################################################################################
#           A Utility Class for Date and Time                                               #
#############################################################################################

class DTime():
    def __init__(self, dtime_str = None):
        if dtime_str == None:
            self.dtime = dt.datetime.now()
        else:
            self.dtime = dt.datetime(dtime_str)

    def getCurrentDate(self) -> str:                                #-> str is just an annotation telling what the method should return, doesn't affect anything
        '''gets current date in string'''
        return str(self.dtime.date())

    def getCurrentTime(self) -> str:
        '''gets current time in string'''
        return str(self.dtime.time())