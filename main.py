from Reading import Read

# import * from Writting

from Operation import DTime, Stock

dt = DTime()

reader = Read()

stk = Stock(dt)

def initialize():
    '''initialize the program'''
    while (True):  #infinite loop
        print(f'''
        Welcome to acer laptop  Shop
{"-"*80}
        Enter 1 To Display
        Enter 2 To Sell laptop
        Enter 3 To Buy laptop
        Enter 4 To Exit
{"-"*80}
        ''')
        try:
            command = int(input("Please select a number from 1 to 4: "))
            if (command == 1):
                stk.showStock()
                command = input("Press Enter to go back to Main Menu!")
            elif (command == 2):
                stk.sell()
                command = input("Press Enter to go back to Main Menu!")
            elif (command == 3):
                stk.buy()  #initialize values of lists of laptop to return
                command = input("Press Enter to go back to Main Menu!")
            elif (command == 4):
                print("Thank you visit again")
                break  #get out of loop
            else:
                print("Invalid input. Please check and try again.")
        except ValueError as error:  #if input can not be parsed
            print(f"Please input a valid number. {error}")

#initialize the program
initialize()
