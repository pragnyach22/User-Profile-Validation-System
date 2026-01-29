fullname=input("Enter your full name: ")
email=input("Enter your email: ")
mobileno=input("Enter your mobile number: ")
age=int(input("Enter your age: "))
valid=True
if(fullname.count(" ")<1 or fullname[0]==" " or fullname[len(fullname)-1]==" "):
    valid=False
elif(email.count("@")<1 or email.count(".")<1 or email[0]=="@"):
    valid=False
elif(mobileno.isdigit()==False or len(mobileno)!=10 or mobileno[0]!=0):
    valid=False
elif( age<18 or age>60):
    valid=False
if(valid):
    print("user is valid")
else:
    print("user is not valid")
