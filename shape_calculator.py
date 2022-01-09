
#
user = input("what shape do wanna calculate : ")
t=("triangle"or "Triangle"or"TRIANGLE")
r=("rectangle"or"Rectangle"or"RECTANGLE")
c=("circle"or "CIRCLE" or"Circle")
s=("square"or "Square"or "SQUARE")
if user==r:
    l1=int(input("LENGTH : "))
    b1=int(input("BREADTH : "))
    print(f"AREA: {l1*b1} ")
    per=2*(l1+b1)
    print(f"PERIMETER : {per} ")
    
elif user==c:
    l2=int(input("RADIUS : "))
    print(f"AREA: {2*3.14*l2*l2} ")
    print(F"PERIMETER : {2*3.14*l2} ")

elif user==s:
    a=int(input("LENGTH : "))
    print(f"AREA: {a**2} ")
    print(F"PERIMETER : {4*a} ")
 
elif user==t:
    t1=int(input("LENGTH 1 : "))
    t2=int(input("LENGTH 2: "))
    t3=int(input("LENGTH 3: "))
    s =(t1+t2+t3)/100
    area3=s*((s-t1)*(s-t2)*(s-t3))
    print(f"AREA: {area3}  ")
    print(F"PERIMETER : {t1+t2+t3} ")
else:
    print("THE SHAPE ISNT AVAILABLE :( ")
print("developer: Aman bangera")