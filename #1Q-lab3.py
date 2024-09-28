#1

numList = []
maxx = 0

for num in range(10):
 number = int(input(f"Enter number {num+1} to find max: "))

 numList.append(number)
 
 if number > maxx:
    maxx = number

print(f"the maximum is: {maxx}!")
    
