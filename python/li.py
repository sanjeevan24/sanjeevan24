
shopping_list = [["Shirt", 2500.0, "Casual"], ["Jeans", 4000.0, "Denim"],["T-Shirt", 1500.0, "Sport"],["Jacket", 6000.0, "Winter"],["Cap", 800.0, "Casual"]]

for item in shopping_list:
    if item[2] != "Casual":
        print(item)
    


item_names = [item[0] for item in shopping_list]
print(item_names)


shopping_list.sort
(key=lambda x: x[1], reverse=True)
print(shopping_list)









