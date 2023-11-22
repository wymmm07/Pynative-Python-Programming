#Exercise 2: Print the sum of the current number and the previous number
#Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.
number = 0
for i in range(10):
    if i == 0:
        print("Current number is", i, "Previous number is", i, "Sum:", i + (i))
    else:
        print("Current number is", i, "Previous number is", i - 1, "Sum:", i + (i - 1))
