a="sanjeevan"
b="sanji6"
attempt=0

while attempt<3:
   username=input("enter the user name:")
   password=input("enter the password:")
   
   if a==username and b==password:
     print("success")
     break
   else:
      print("try again")
      attempt=attempt+1
else:
    print(" failed ")
    
   




        






