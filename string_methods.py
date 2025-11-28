#string methods 

text=" Hey 143, hey!!, hello, how are you doing today?  " 
print("Text:",text) 

#remove spaces -strip()
print("strip() : ",text.strip()) #strip()-removes any leading and trailing spaces
#used in ml processing to clean text cause in real data(CSVs,files),extra spaces cause bugs

#upper and lower case 
print("upper() : ",text.upper()) #converts everything to capital letters 
print("lower() : ",text.lower()) #converts everything to small letters 
#used in normalization of text data

#title case 
print("title() : ",text.title()) #each word starts with a capital letter 
#uses-formatting names,display headings

#replace text 
print("replace(): ",text.replace("today","tonight!!!!"))

t=" aaa aaaa a aaaaa a aa"
print("replace(): ",t.replace("aa","b")) #string are immutable.so replace()-dosent change original it returns new version
#real_uses: clean specific words,fix typos 

#counting words 
print("count of 'o' : ",text.count('o'))
#another example of counting and replacing
string="banana"
print(string.count("a"))
print(string.count("na"))
print(string.replace("na","ha"))

#split() and join()
s="how tou doing "
w=s.split() 
print("words: ",w)
print("joined words: ","-".join(w)) 


print("split: ",text.strip().split()) 
words=text.strip().split()
print("joined with '-':","-".join(words)) 

print("replace 'hello' with 'hi': ",text.replace("hello","hi")) 
print("count 'e': ",text.count("e"))