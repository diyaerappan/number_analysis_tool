numbers=[]
n=int(input("How many numbers do you want to enter?"))
for i in range(n):
    num=int(input("Enter a number:"))
    numbers.append(num)
largest=max(numbers)
smallest=min(numbers)
total=sum(numbers)
average=total/n
print("\n-------Results-------")
print("Numbers:",numbers)
print("Largest:",largest)
print("Smallest:",smallest)
print("Sum:",total)
print("Average:",average)