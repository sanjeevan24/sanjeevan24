print("===menu===")
print("1.checking banking")
print("2.withdrow")
print("3.deposit")
print("4.view all account")
print("5.exit")

option=int(input("choice one(1-5):"))
if 1<=option and option<=5:
    while option <=4:
      print("===menu===")
      print("1.checking banking")
      print("2.withdrow")
      print("3.deposit")
      print("4.view all account")
      print("5.exit")  
      option=int(input("choice num:"))
    else:
      print("thank you sir")
    
else:
    print("incorrect")

