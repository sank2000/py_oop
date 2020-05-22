class Phone:
    def __init__(self, color):
        self.clr = color.capitalize()
        self.phoneDetails()

    def phoneDetails(self):
        print('Model :  {} {}'.format(self.brand, self.model))
        print('Color : ', self.clr)
        print('Price : ', self.price)
        self.product = self.brand + self.model + ' ' + self.clr
        book = input('\nBook Now? (Y/N) ')
        print('=======================================\n')
        return self.buyNow() if book in 'Yy' else None

    def buyNow(self):
        print('==++++++++== My Cart ==++++++++==')
        print('Product(s) you\'ve chosen to buy:')
        print(self.product, '\t $', self.price)
        print('Amount will be collected when the product is delivered')
        cnf = input('Enter C to Confirm: ')
        if cnf in 'Cc':
            print('> Thanks for shopping with us, your shipment is on the way!')
        print('========================================\n')

class Google(Phone):
    def __init__(self, clr, model, price):
        self.price = price
        self.model = model
        self.brand = 'Google'
        super().__init__(clr)

class Asus(Phone):
    def __init__(self, clr, model, price):
        self.price = price
        self.model = 'Zenfone ' + model
        self.brand = 'Asus'
        super().__init__(clr)

class MaxProM1(Asus):
    def __init__(self, clr):
        model = 'Max Pro M1'
        self.code = 'X00T'
        self.memory = '4 GB, 64 GB'
        price = 249
        super().__init__(clr, model, price)

class Pixel4XL(Google):
    def __init__(self, clr):
        model = 'Pixel 4 XL'
        self.code = 'vento'
        self.memory = '6 GB, 128 GB'
        price = 699
        super().__init__(clr, model, price)

class MaxProM2(Asus):
    def __init__(self, clr):
        model = 'Max Pro M2'
        self.code = 'X00B'
        self.memory = '4 GB, 64 GB'
        price = 279
        super().__init__(clr, model, price)

class Pixel4(Google):
    def __init__(self, clr):
        model = 'Pixel 4'
        self.code = 'clamens'
        self.memory = '6 GB, 64 GB'
        price = 649
        super().__init__(clr, model, price)


print('\n +++++++++++++++++++++++++++++++++')
print('[  CONSOLE CART, THE PHONE DEALER  ]')
print(' +++++++++++++++++++++++++++++++++')


MyPhone = Pixel4('glassy black')
MyPhone2 = MaxProM2('black')
