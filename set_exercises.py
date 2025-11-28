#one-unique words in a sentence 
sentence="I am am learning python python" 
words=sentence.split()
unique_words=set(words) 
print("unique words are: ",unique_words) 

#second-check if any two lists have any common elements 
l1=[1,2,7,9]
l2=[5,6,7,8] 
common_elements=set(l1)&set(l2) 
if common_elements:
    print("common elements are: ",common_elements) #in my code i didnt write conditional statements ,i only wrote print("common elements are")
else:    
    print("No common elements") 

#find elemets that are both lists and not both lists 
a=[1,2,7,9]
b=[5,6,7,8] 
common=set(a)&set(b)
notcommon=set(a)^set(b)
print("common: ",common) 
print("not common: ",notcommon)

#remove duplicates from a list without using a list 
list=[1,2,4,2,3,4,5,5,6,6,7,34,5,36,4,44,34]
unique_list=[]
for num in list:
    if num not in unique_list:
        unique_list.append(num) 
print(unique_list)