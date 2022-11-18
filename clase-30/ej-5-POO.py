


# --------- Start Class client----------


class Client:

    def __init__(self, name):
        self.name = name
        self.mount = 0

    def deposit(self, mount):
        self.mount += mount

    def extract(self, mount):
        self.mount -= mount

    def return_mount(self):
        return self.mount

    def __str__(self):
        return f'{self.name}\t $ {self.mount}'


# --------- End Class client----------


class Bank:

    def __init__(self, name, residence):
        self.name = name
        self.residence = residence
        self.client1 = Client('Lucas')
        self.client2 = Client('Maria')
        self.client3 = Client('Pedro')

    def __str__(self):
        return f'{"-"*20}\nBanco {self.name} - {self.residence}\n{"-"*20}'

        
    def operar(self):
        self.client1.deposit(100)
        self.client2.deposit(200)
        self.client3.deposit(300)
        self.client3.extract(50)

    def deposit_total(self):
        print(self.client1)
        print(self.client2)
        print(self.client3)
        
        print("="*10)
        total = self.client1.return_mount()+self.client2.return_mount()+self.client3.return_mount()
        print(f'total\t ${total}')

bank1 = Bank('Bank of america', 'av acon 123')

print(bank1)
bank1.operar()
bank1.deposit_total()
