#==========================================================

print("/n welcome to uor bank.\n")
admin_name=input("enter the name :")
admin_id=input("enter admin id :")
admin_password=input("enter the admin password :")


with open("admin.txt",'w') as file:
 file.write(f"{admin_name}\t{admin_id}\t{admin_password}")

print("admin account created succesfully...\n ")






with open("admin.txt",'r')as file:
    new=file.read()


# admin_id=input("enter your id to continue :")
# admin_password=input("enter your password :")


# def admin_list():
#     while true:
        
#             print("\n----MENU----")
#             print("1.account create")
#             print("2. deposit")
#             print("3.withdrow money")
#             print("4.cheak balance")
#             print("5.transaction history")
#             print("6.exit")
                                    
#     else:
#             print("admin not found")
#             choice=input("enter the num(01-10)") 

#         if choice ==1:
#             createname=input('enter thye nname')

        
#          if choice==2:
#                 deposit=int(input("enter the deposit amount:"))
#                    depops 


# def create_customer():
#     account_auto_num=1000
#     custer_name=input("enter new customer name:")
            
