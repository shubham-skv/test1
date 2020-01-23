largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if(num=='done'):
        break
    try:
        num1=int(num)
    except:
        print("Invalid input")
        continue
    if(smallest==None):
        smallest=num1
    if(largest==None):
        largest=num1
    if(smallest>num1):
        smallest=num1
    if(largest<num1):
        largest=num1
    

print("Maximum", largest)
