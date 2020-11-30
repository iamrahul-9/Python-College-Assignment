my_list = [1,5,4,45,87,90,8,11,5,3] 
print(f"Print the list\n{my_list}")

list2 = [40,12,17] 

my_list.append(15)
print(f"Add 15 at the end of the list\n{my_list}") 

my_list.extend(list2) 
print(f"Combining two list together\n{my_list}") 

my_list.insert(-1,80)
print(f"Insert new item 80 in the list\n{my_list}") 

x = my_list.index(5)
print(f"Print the index no. of the item\n{x}")

my_list.sort()
print(f"Sorted list\n{my_list}")