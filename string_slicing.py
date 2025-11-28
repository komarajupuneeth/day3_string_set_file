#STRING SLICING 
#slicing is how you extract parts of sequences 
#  syntax: string[start(inclusive):stop(exclusive):step(default is 1)]
#works on string,lists,tuples
s="PYTHON" 
print(s[0:2]) 
print(s[2:]) 
print(s[:4]) 
print(s[-3:]) 
print(s[::-1])

#extract last n chars 
file="data.csv"
print(file[-3:]) 
phone="45879865467" 
print(phone[-4:]) 

#skipping characters with step 
print(file[1:7:2]) 
print(file[3:8:3]) 

#reverse substring 
print(s[1:5]) 
print(s[1:5][::-1]) #or 
print(s[4:0:-1])