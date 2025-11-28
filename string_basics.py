#string basics 

name="clark kent" 
print("name:",name) 

#strings are sequences 
print("first_char:",name[0].upper())
print("last_char:",name[-1]) 

#loop through string 
for char in name:
    print(char) 

# name[0]="k" #string are immutable