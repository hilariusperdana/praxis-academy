def start() :
    print ("Welcome to the converter toolkit made by Alan.")
    op = input ("Please input what operation you wish to perform. 1 for Fahrenheit to Celsius, 2 for meters to centimetres and 3 for megabytes to gigabytes")

if op == "1":
    f1 = input ("Please enter your fahrenheit temperature: ")
    f1 = int(f1)

    a1 = (f1 - 32) / 1.8
    a1 = str(a1)

    print (a1+" celsius") 

elif op == "2":
    m1 = input ("Please input your the amount of meters you wish to convert: ")
    m1 = int(m1)
    m2 = (m1 * 100)

    m2 = str(m2)
    print (m2+" m")


if op == "3":
    mb1 = input ("Please input the amount of megabytes you want to convert")
    mb1 = int(mb1)
    mb2 = (mb1 / 1024)
    mb3 = (mb2 / 1024)

    mb3 = str(mb3)

    print (mb3+" GB")

else:
    print ("Sorry, that was an invalid command!")

start()