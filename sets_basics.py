#theory- A set is an unordered,unique(no duplicates),mutable(u can add or remove elements),
# fast for search (0(1)-average time) 


#set creation
s={1,2,3,4,5,4,4,4}
print(s) #duplicates are removed 

#add items 
s.add(10)
print("after adding: ",s)

#remove items 
s.remove(3) #if element not present it gives error 
print("after removing: ",s) 

#discard 
s.discard(50) #doesnt throw error

#membership checking(very fast)
print(2 in s) 
print(100 not in s) 
print(100 in s)