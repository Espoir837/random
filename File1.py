name=input("name=")
age=input("age=")
f_number=input("favorite_number=")
age=int(age)+10
f_number=int(f_number)
X=""
if f_number%2==0:
    X='even'
elif f_number%2==1 and f_number!=1:
    X='odd'
else:
    X="not even or odd"
f_number=int(f_number)**2
print(f"Hi {name}! In 10 years you will be {age}. Your favorite number squered is {f_number}, and it is {X}.")

