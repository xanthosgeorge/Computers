listapragmatwn = {}
#Εισαγωγή αντικειμένων στο Dictionary 
while True: 
    listapragmatwn[input("Δώστε το αντικείμενο που θέλετε να βάλετε στη λίστα \n")] =input("Δώστε τιμή του αντικείμενου \n")
    x=input("Επιθυμήτε να σταματήσετε τη διαδικασία πρόσθεσης ?? \n")
    if (x=="yes"):
        break
#Δημιουργία λίστας με τις τιμές του Dictionary
listapragmatwn_list=list(listapragmatwn.values())
print(listapragmatwn_list)
s=0
#Υπολογσιμός του συνολικού κόστους 
for i  in range(0,len(listapragmatwn_list)):
    s=s+float(listapragmatwn_list[i])
kostos = s *1.24
print(kostos)


