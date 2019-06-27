class AccountException(Exception):
    pass

class AccountBalanceException(AccountException):
    pass

class FrozenAccountException(AccountException):
    pass

class InvalidTransactionException(AccountException):
    pass



""" if + raise """
class Account():
    def __init__(self, balance, is_frozen):
        self.balance = balance
        self.is_frozen = is_frozen
    
    def check(self):
        #조회
        print("계좌 잔액은 {0}원 입니다.".format(self.balance))
    
    def deposit(self, amount):
        #입금
        if amount > 0:
            self.balance += amount
        else:
            raise InvalidTransactionException("0 이하의 액수는 입금할 수 없습니다.")
    
    def withdraw(self, amount):
        #출금
        if self.is_frozen == True:
            raise FrozenAccountException("동결된 계좌에서 출금할 수 없습니다.")
        elif amount <= 0:
            raise InvalidTransactionException("0 이하의 액수는 출금할 수 없습니다.")
        elif amount > self.balance:
            raise AccountBalanceException("계좌 잔액이 부족합니다.")
        else:
            self.balance -= amount

