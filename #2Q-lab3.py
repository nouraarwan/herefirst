#2Q-lab3

num = int(input("input a number: "))
print(f" the square of numbers from 1 to {num}:")

for i in range(1,num+1):
    squer = lambda x: x * x
    print(f"{i}={squer(i)}")