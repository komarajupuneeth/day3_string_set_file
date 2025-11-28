#first question 
string="puneeth" 
rev_string=""
for char in string:
    rev_string=char+rev_string
print("reverse string is :",rev_string) 
print()

#second question-vowels in a string 
s="eManUiEl" 
s=s.lower()
for char in s: 
    if char in "aeiou":
       print(char,end=",") 
print()
print()

#q-3 :-take a sentence as input and print-no.of words and no.of chars 
sentence="  what are you looking at mf  "
# my_mistake 
# print("no.of words: ",sentence.split())
# print("no.of character: ",sentence.replace(" ","")) 
words=sentence.split() 
chars_without_space=sentence.replace(" ","")

print("sentence: ",sentence)
print("no.of words: ",len(words))
print("no.of chars (no spaces): ",len(chars_without_space)) 
print()

#q-4 :--- check if string is palindrome or not  
sen="MaDAm" 
sen=sen.lower()
rev_sen=sen[::-1] 
if sen==rev_sen:
    print("Is a Palindrome") 
else:
    print("Is Not a Palindrome")