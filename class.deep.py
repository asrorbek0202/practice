'''
class deep diving
1. encapsulation
2. inheritence
3. polimorphism
'''

print("===== encapsulation =====")

'''C++ , JAVA > public,private,protected
PHP Typscript >  public,private,protected
PYTHON >.  __name  ==> private.   _name  ==> protected  , name ==> public
'''


class Accaunt():

    # state
    description = "The class makes bank accaunt"

    # constructor
    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount

     # method
    def get_balance(self):
        print(f"the owner {self.__owner} has {self.__amount} usd")

    def deposit(self, amount):
        print("deposit", amount)
        self.__amount += amount

    def withdraw(self, amount):
        print("withdraw", amount)
        self.__amount -= amount

    @property
    def holder(self):
        return self.__owner

    @holder.setter
    def holder(self, new_owner):
        print("holder.setter", new_owner)
        self.__owner = new_owner

    def change_ownership(self, new_owner):
        print("change_ownership", new_owner)
        self.__owner = new_owner


my_accaunt = Accaunt("Shawn", 1000)
my_accaunt.get_balance()

print("-----")
my_accaunt.deposit(3500)
my_accaunt.withdraw(400)
my_accaunt.get_balance()

try:
    result = my_accaunt.__amount
    print(result)
except Exception as err:
    print("NO target state found", err)

accaunt_owner = my_accaunt.holder
print("result", accaunt_owner)

my_accaunt.change_ownership("Steve")
print("new owner", my_accaunt.holder)


my_accaunt.holder = ("Martin")
