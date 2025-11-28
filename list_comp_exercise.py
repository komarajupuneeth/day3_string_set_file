##1.create a list of squares for  numbers 1 to 20 
list_of_squares=[n**2 for n in range(1,21)]
print(list_of_squares)

##extract only words longer than 3 letters from a sentence 
sentence="hi how are you doing myfriend" 
words=sentence.split()
long_words=[w    for w in words   if len(w)>3] 
print(long_words) 

##from a list of numbers,create 1.even numbers list 2.odd numbers list 
nums=[1,2,3,4,5,6,12,234,45632,23423745,67,856744,3,67,2,56] 
even_nums=[n   for n in nums  if n%2==0]
odd_nums=[n  for n in nums if n%2!=0] 
print(even_nums)
print(odd_nums) 


##given a list of strings,convert tem all into except those already in lowercase 
list=["wHo","whAt","whY","When","WHOM"]
result=[s    if  s.islower()  else  s.lower()  for s in list] 
print(result)


##flatten a 2d list using comprehension 
nested=[[1,2],[3,4],[5,6]] 
flat=[num for sublist in nested  for num in sublist ]
print(flat)
## another way is  
flat=[]
for sublist in nested:
    for num in sublist:
        flat.append(num) 
print(flat)