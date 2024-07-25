MAX_WIDTH = 125
BILL_TABLE_FORMAT = "{:<8} {:<20} {:<20} {:<15} {:<15} {:>10} {:>15} {:>15}"
SUMMARY_FORMAT = "{:>85} : {:>20}   Rs.{:>10}\n"
CUSTOMER_FORMAT = "{:<25} {:<55} {:<25} {:<35}\n"

class Write:
    def __init__(self, path=None):
        print('Writing Module initialized!')
        self.path = path

    def setPath(self, path):
        self.path = path

    def updateStock(self, items):
        print('Changing stock file:', self.path)
        with open(self.path, 'w') as fp:
            for item in items:
                fp.write(','.join(map(str, item)) + '\n')

    def writeBill(self, customer_info):
        with open(self.path, 'w') as f:
            f.write(f"{'acer laptop Shop'.center(MAX_WIDTH, ' ')}\n")
            f.write(f"{'sinamangal, Kathmandu, Nepal'.center(MAX_WIDTH, ' ')}\n")
            customer_text = CUSTOMER_FORMAT.format("Customer's Name:", customer_info['customer_name'], "Date:", customer_info['current_date'])
            f.write(customer_text.center(MAX_WIDTH, ' ') + '\n')
            customer_phone = CUSTOMER_FORMAT.format("Customer's Phone Number:", customer_info['phone_number'], "Time:", customer_info['current_time'])
            f.write(customer_phone.center(MAX_WIDTH, ' ') + '\n')
            f.write('-' * MAX_WIDTH + '\n')
            f.write(BILL_TABLE_FORMAT.format('S.No.', 'Company', 'Name', 'CPU', 'GPU', 'Price', 'Quantity', 'Amount') + '\n')
            f.write('-' * MAX_WIDTH + '\n')

    def finalBill(self, details):
        shipping = float(details['shipping'])
        bill_total = float(details['total_amount'])
        grand_total = shipping + bill_total
        vat_amount = grand_total * 0.13
        net_amount = grand_total + vat_amount
        with open(self.path, 'a') as f:
            f.write('-' * MAX_WIDTH + '\n')
            f.write(SUMMARY_FORMAT.format('Shipping Cost', details['route'], shipping))
            f.write(SUMMARY_FORMAT.format('Grand Total', 'Items: ' + str(details['total_items']), round(grand_total)))
            f.write(SUMMARY_FORMAT.format('VAT', '13%', round(vat_amount)))
            f.write(SUMMARY_FORMAT.format('Final Total', '', round(net_amount)))
            f.write('-' * MAX_WIDTH + '\n')
            f.write("Note: Goods Once Sold will not be returned in any condition!\n")
            f.write('-' * MAX_WIDTH + '\n')

    def addItem(self, item):
        with open(self.path, 'a') as f:
            f.write(BILL_TABLE_FORMAT.format(item['count'], item['company_name'], item['item_name'], item['cpu'], item['gpu'], item['price'], item['quantity'], 'Rs. ' + str(int(item['price']) * int(item['quantity']))) + '\n')

    def writeBuy(self, vender_info):
        with open(self.path, 'w') as f:
            f.write(f"{'acer laptop shop'.center(MAX_WIDTH, ' ')}\n")
            f.write(f"{'sinamangal, Kathmandu, Nepal'.center(MAX_WIDTH, ' ')}\n")
            f.write('\n')
            customer_text = CUSTOMER_FORMAT.format("Vender's Name:", vender_info['vender_name'], "Date:", vender_info['current_date'])
            f.write(str(customer_text.center(MAX_WIDTH, " ")))
            customer_phone = CUSTOMER_FORMAT.format("Vender's Phone Number:", vender_info['phone_number'], "Time:", vender_info['current_time'])
            f.write(str(customer_phone.center(MAX_WIDTH, " ")))
            f.write(str('-' * MAX_WIDTH) + '\n')
            f.write(BILL_TABLE_FORMAT.format('S.No.', 'Company', 'Name', 'CPU', 'GPU', 'Price', 'Quantity', 'Amount'))
            f.write('\n' + str('-' * MAX_WIDTH) + '\n')

    def finalBuy(self, details):
        shipping = float(details['shipping'])
        bill_total = float(details['total_amount'])
        grand_total = shipping + bill_total
        vat_amount = grand_total * 0.13
        net_amount = grand_total + vat_amount
        with open(self.path, 'a+') as f:
            f.write(str('-' * MAX_WIDTH) + '\n')
            f.write(SUMMARY_FORMAT.format('Transport Cost', details['route'], shipping))
            f.write(SUMMARY_FORMAT.format('Grand Total', 'Items: ' + str(details['total_items']), round(grand_total)))
            f.write(SUMMARY_FORMAT.format('VAT', '13%', round(vat_amount)))
            f.write(SUMMARY_FORMAT.format('Final Total', '', round(net_amount)))
            f.write(str('-' * MAX_WIDTH) + '\n')
            f.write("Note: Goods Once Sold will not be returned in any condition!\n")
            f.write(str('-' * MAX_WIDTH) + '\n')
