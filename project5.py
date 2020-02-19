f = open("project.txt", "r")
# Άνοιγμα αρχείου
words = f.read()
words = words.split()
print (words)
for i in range(0,len(words)):
    if len(words[i])>3:
        # Αφαίρεση πρώτου γράμματος
        tomi = words[i][:-(len(words[i])-1)]
        #print(tomi)
        # Βάζουμε τα γράμματα όπως τα ζητάει η εκφώνηση
        prosthiki = words[i][1:] +tomi +"ay"
        print(prosthiki)
