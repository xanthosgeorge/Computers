import datetime
x = datetime.datetime.now()
givendate = input("Δώστε μια ημερομηνία σε μορφή ΗΗ\ΜΜ\ΕΕΕΕ")
# Κάνουμε ακέραιες μεταβλητες μερη του input
givendate_year = int(givendate[6:10])
givendate_month = int(givendate[3:5])
givendate_day = int(givendate[0:2])
#Με τη χρήση module καθορίζουμε την τωρινη ημερομηνια και με συναρτήσεις κάνουμε την αφαίρεση ανάμεσα στις δύο ημερομηνίες
someday = datetime.date(givendate_year,givendate_month,givendate_day)
today = datetime.date(x.year,x.month,x.day)
dif = today - someday
print ("Απο την δοθείσα ημερομηνία έχουν παρέλθει/υπολείπονται:")
print (abs(dif.days),"μέρες")
print (x.hour , "ώρες")
print (x.minute , "λεπτά")
print (x.second , "δευτερόλεπτα")
# Αλγόριθμος εύρεσης δίσεκτου έτους
if givendate_month==2:
    if givendate_year%4==0:
        if givendate_year%100==0:
            if givendate_year%400==0:
                print("Ο μήνας της δοθείσας ημερομηνίας  έχει 29 μέρες")
            else:
                print("Ο μήνας της δοθείσας ημερομηνίας  έχει 28 μέρες")
        else:
            print("Ο μήνας της δοθείσας ημερομηνίας  έχει 29 μέρες")
    else:
        print("Ο μήνας της δοθείσας ημερομηνίας  έχει 28 μέρες")
else:
    if givendate_month<=7 and (givendate_month%3==0 or givendate_month==1):
        print("O μήνας της δοθείσας ημερομηνίας έχει 31 ημέρες ")
    elif givendate_month<=7 and givendate_month%2==0:
        print("O μήνας της δοθείσας ημερομηνίας έχει 30 μέρες")
    elif givendate_month>=8 and givendate_month%2==0:
        print("O μήνας της δοθείσας ημερομηνίας έχει 31 ημέρες")
    elif givendate_month>8 and givendate_month%3==0:
        print("O μήνας της δοθείσας ημερομηνίας έχει 30 ημέρες")




