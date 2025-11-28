###1.list comprehension -a short ,clean ,fast way to way to create lists 
#normal loop 
result=[]
for x in range(10):
    result.append(x**2) 
#list comprehension 
result=[x*2 for x in range(10)] 

###2.basic syntax----------[expression    for item in iterable]
nums=[x for x in range(10)] 
print(nums)

###3.adding condition ----------[expression    for item in iterable     if condition ] 
evens=[x   for x in range(10)   if x%2==0 ] 
print(evens)

###4.transforming data 
nums=[1,2,3,4]
squares=[n*n for n in nums]
print(squares)

####5.strings in comprehensions 
text=" hello "
chars=[c.upper()  for c in text.strip()] #we can use strip to remove the spaces at beginnig and ending 
print(chars)

###6. list comprehension with if - else ,,, syntax------[exp1  if condition  else  exp2      for item in iterable]  
nums=[1,2,3,4,5]
labels=[" even "  if n%2==0  else " odd "    for n in nums ] 
print(labels,"\n")

###7.nested looops in comprehensions 
pairs=[(i,j)     for i in range(3)   for j in range(3)] 
print(pairs,"\n")


############ real world example  -cleaning data
names=["   rajput  ","jOHN  ","  alice  ","BOBBY"] 
cleaned_data=[n.strip().title()    for n in names] 
print(cleaned_data)