print("Count to 10!")
for x in range (0, 11):
    print(x)


print("Count to 20!")
for x in range (0, 21):
    print(x)

Total = int(input("What number do you want me to count to? "))
print("Let's start from 0 to {}.".format(Total))
for x in range (0, Total + 1):
    print(x)