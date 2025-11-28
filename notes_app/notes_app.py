#notes app
def write_notes(text): #defines a function that expects 1 input:text
    with open("notes.txt","a") as f: #"notes.txt"-file name,"a"-append mode ,"as f"-creates a temp file object named f
        f.write(text + "\n")         #the "with" statement automaticallu closes file when done 

def read_notes():              #reads all notes from notes.text and prints them nicely
    with open("notes.txt","r") as f:       #opens the file to read 
        notes=f.readlines()            #this reads the entire file ,but returns list where each element is one line 
        for n in notes:                #notes is a list of strings ,and n loops throug hth elsit
            print(n.strip())           #.strip(),removes -newline\n,spaces ,tabs 

write_notes("day3:learning file handling ")
write_notes("this feels easy now") 
print("your notes:") 
read_notes()
