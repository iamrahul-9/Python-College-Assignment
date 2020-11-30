tuple_names = ("rahul","amit","sahil","pratik","shubham")
tuple_number = (1,5,4,8,3,6,4,5,9,8,7,3,2,1,9,5)

print(tuple_names,tuple_number) #print the tuple
print(tuple_names[0]) #print the first item in the tuple using index
print(tuple_names[-1]) #print the last item using negative indexing
print(len(tuple_number)) #print the number of items in the tuple
print(tuple_number[5:8]) #prints the items between index using slicing 
print(tuple_number.count(5)) #Return the number of times the value appears in the tuple
print(tuple_number.index(9)) #Search for the first occurrence of the value, and return its position
