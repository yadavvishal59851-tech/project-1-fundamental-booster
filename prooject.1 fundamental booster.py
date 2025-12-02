print("Welcome to the interactive Personal Data Collector!")

Name = input("please enter your name: ")
age = input("please emter your age: ")
height = input("please enter your height in meters : ")
number = input("please enter your favourite number: ")

print("thank you! Here is the information we collected:")

print("Name: ",(Name),type(Name),id(Name))
print("age: ",(age),type(age),id(age))
print("height: ",(height),type(height),id(height))
print("number: ",(number),type(number),id(number))

birthyear = 2025 - age
print(f"your birthyear is approximately: {birthyear}")


print("Thank you for using the personal Data Collector." )
print("wish you best of luck and good bye")

