


# def get_number():
#     return 5

# def set_number(num):
#     number = num
#     print("From set_number, num is: ", str(num))
#     return number


# num = get_number()
# set_number(6)

# print("End of Program, Num is: ", str(num))


# def add_number(num1, num2):
#     print("num1: ", str(num1))
#     print("num2: ", str(num2))
#     val = num1 + num2
#     print("from add_number, val is: ", str(val))
#     return val


# output = add_number(2, 5) # 7

# print("Output of {} and {} is {}.".format(str(2), str(5), output))



# def get_firstname(full_name): # Dionicio Gonzalez
#     space = full_name.index(" ")
#     first_name = full_name[:space]
#     return first_name

# # my_name = get_firstname("Dionicio Gonzalez")
# # print("Hello, my name is " + my_name + ".")


# names = [
#     "Dionicio Gonzalez", 
#     "Joe Biden", 
#     "Mike Tyson", 
#     "Tom Brady", 
#     "Kobe Bryant"
# ]

# for name in names:
#     # print("Name: ", name)
#     my_name = get_firstname(name)
#     # print("Hello, my name is " + my_name + ".")
#     # print(my_name == "Tom")
#     if my_name == "Tom":
#         print(my_name + " plays football!")
#     elif my_name == "Kobe":
#         print(my_name + " plays basketball!")
#     elif my_name == "Mike":
#         print(my_name + " is into boxing!")
#     else:
#         print(my_name + " is not not into sports!")



# def pay(wage, hours):
#     amount = 0
#     if hours <= 40:
#         print("Here!")
#         amount = wage * hours
#     else:
#         amount = (wage * 40) + ((1.5) * wage * (hours - 40))
#     return amount

# hourlyWage = eval(input("Enter the hourly wage: "))
# hoursWorked = eval(input("Enter the numbers of hours worked: "))

# result = pay(hourlyWage, hoursWorked)
# print("Earnings: ${0:,.2f}".format(result))


# def isVowelWord(word):
#     word = word.upper()
#     vowels = ('A', 'E', 'I', 'O', 'U')
#     for vowel in vowels:
#     #     if vowel not in word:
#     #         return False
#     # return True 
#         vowel in word

# word = input("Enter a word: ")

# if isVowelWord(word) :
#     print(word, "contains vowel. ")
# else:
#     print(word, "does not contain vowel. ")


# def main():
#     x = 2
#     print(str(x) + ": function main")
#     trivial()
#     print(str(x) + ": function main")

# def trivial():
#     x = 3
#     print(str(x) + ": function trivial")

# main()

