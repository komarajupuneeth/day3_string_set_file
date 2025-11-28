#removes duplicates from a list
numbers=[1,2,3,3,2,4,4,5]
unique_numbers=list(set(numbers)) 

print("original: ",numbers)
print("unique: ",unique_numbers) #used in every ml projects when you clean the data

#SET OPERATIONS
a={1,2,3,4}
b={3,4,5,6}

print("union: ",a | b) 
print("intersection: ",a & b)
print("difference: ",a - b)
print("systematic difference: ",a ^ b)
#they appear in ml pipelines ,feature engineeing, interviews  

#check if two lists share any elements 
l1=[1,2,3]
l2=[3,8,9]
common=set(l1)&set(l2) 
if common:
    print("common elements: ",common) 
else:
    print("NO common elements")