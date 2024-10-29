cyclist1=int(input("racer1= how fast is he running:"))
cyclist2=int(input("racer2= how fast is he running:"))
cyclist3=int(input("racer3= how fast is he running:"))
avg =(cyclist1+cyclist2+cyclist3)/3
print("the average speed is:",avg)
if (cyclist1>avg):
    print("racer1 is the fastest😉")
elif (cyclist2>avg):
    print("racer2 is the fastest😉")
elif (cyclist3>avg):
    print("racer3 is the fastest😉")