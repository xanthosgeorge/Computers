import datetime
x = datetime.datetime.now()
givendate = input("Δώστε μια ημερομηνία σε μορφή ΗΗ\ΜΜ\ΕΕΕΕ")
givendate_year = int(givendate[6:10])
givendate_month = int(givendate[3:5])
givendate_day = int(givendate[0:2])
someday = datetime.date(givendate_year,givendate_month,givendate_day)
today = datetime.date(x.year,x.month,x.day)
dif = today - someday
print ("Απο την δοθείσα ημερομηνία έχουν περάσει/υπολείπονται:")
print (abs(dif.days),"μέρες")
print (x.hour , "ώρες")
print (x.minute , "λεπτά")
print (x.second , "δευτερόλεπτα")
import calendar
y = int(givendate_year)
m = int(givendate_month)
print(calendar.month(y, m))


