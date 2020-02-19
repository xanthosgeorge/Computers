while True:
    # Έλεγχος εγκυρότητας τιμής
    x =input("Δώστε ενα εριθμό που να μήν είναι μονοψήφιος")
    if int(x)%10!=int(x):
        break
adder=int(x)
limit = len(x)
sum=0
divider = int(x)
for x in range (0,limit+1):
    sum = sum +divider%10
    divider = divider//10
sum2 = 0
while True:
    sum2 = sum2 + adder*3+1+sum
    adder= adder//10
    if adder%10==adder:
        break 
print(sum2)   


    
   
     

    
