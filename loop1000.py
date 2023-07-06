# Created a progarm that prints out all the even numbers from 1 to 1000

# print out all the numbers from 1 to 1000 using for loop
print("step1")
for num in range (1,1000):
    print(num)

# prints out all the even numbers from 1 -1000 using for loop, % 2
print("step2")
for num in range (1,1000):
    if num % 2 == 0 :
        print(num)