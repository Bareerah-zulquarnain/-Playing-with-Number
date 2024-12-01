number=int(input("enter your number"))

orginal_number= number
reversed_number= 0

while number >0:
    digit = number %10
    reversed_number=reversed_number*10 +digit 
    number //=10

if orginal_number==reversed_number:
    print(f"{orginal_number}is a palidrome")
      
else:
    
    print(f"{orginal_number}is not a palidrome")