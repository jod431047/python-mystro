class User:
    def __init__(self,name,age):
        print(f'welcome {name}')
        self.name =name
        self.age = age


    def show_details(self):
            print(f'Name :{self.name}')
            print(f'Age : {self.age}')

class Bank(User):
    def __init__(self,name,age):
        super().__init__(name,age)
    self.balance = 0
    def withdraw(self,amount):
        if amount > self.balance:
            print(f'you do not have enough balance :{self.balance}')
            return
    self.balance -=amount
    self.show_balance()

    def deposite(self,amount):
        self.balance += amount
        self.show_balance()


    def show_balance(self):
        print(f'your corrent balance :{self.balance}')



c1 = Bank('ahmad' , 23)

c1.withdraw(200)
c1.withdraw(200)
c1.withdraw(100)

c1.show_details()
c1.show_balance()
