f = open("project.txt", "r")
# file open
words = f.read()
words = words.split()
print (words)
for i in range(0,len(words)):
    if len(words[i])>3:
        #Cutting the first letter
        tomi = words[i][:-(len(words[i])-1)]
        #print(tomi)
        #we put all the letters tohether
        prosthiki = words[i][1:] +tomi +"ay"
        print(prosthiki)
