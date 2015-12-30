oInput = int(input("Saisissez un nombre afin de voir sa table de multiplication: "))
oInput2 = int(input("Saisissez le multiplicateur maximum: "))
for i in range (oInput2):
    print (str(i),":", str(oInput), "*", str(i), "=", oInput*i)
oInput3 =""
while not oInput3 == "o":
    oInput3 = input("Voulez-vous quitter le programme? o/n")
print "Aurevoir!"
