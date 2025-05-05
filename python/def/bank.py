balance=50000


def withdrow():
    global balance
    
    amount=int(input('enter the amount:'))
    balance=balance-amount
    print('with drow:', amount)
    print('balance:',balance)
withdrow()
withdrow()