#how to write to a file  
with open("example.txt","w")as f: #"w"-write mode ,creates a file if not exists,overwrites file every time ,with--automaticallu closes file 
    f.write("  Hello Puneeth\n   ")    #f.write()- writes text inside the file 
    f.write("    learning file handling.\n") #USES--- to save logs,save model output,save  results,write config files

# reading a file 
# read enttrie content 
with open("example.txt","r") as f: #"r"-- read mode
    content=f.read()                # .read()--returns everything as one long string
print("file content: ")             #works well for small/median files
print(content)                      #not preferred for huge files
          
#read line by line 
with open("example.txt","r")as f:   #.strip()--removes spaces/newline\n ,loops through file line by line
    for line in f:
        print("line:",line.strip()) 

#appending a file 
with open("example.txt","a") as f:       #"a"mode doesnt delete content ,it just adds new lines to the end 
    f.write("This line was appended.\n")  #uses-for adding logs,adding user messages,updating reports,storing entries