# def main():
#     first()
#     print(str(4) + ": from function main")

# def first():
#     print(str(1) + ": from function first")
#     second()
#     print(str(3) + ": from function first")

# def second():
#     print(str(2) + ": from function second")

# main()


# list1 = ["a", "e", "i", "o", "u"]
# list2 = []

# def f(y):
#     return y.upper()

# for x in list1:
#     print("x: ", x)
#     list2.append(f(x))


# list2 = [f(x) for x in list1]
# print("List: ", [x.upper() 
#     for x in ["a", "e", "i", "o", "u"] if x in ["i", "o"]])

def total(arg1, arg2, arg3=10, arg4=20): 
    return (arg1 ** arg2) + arg3 + arg4

total(2, 3)
total(2, 3, 4)
total(2, 3, 3, 4)
# total(2, 3, 3, 4, 5)

var1 = 2
var2 = 3

total(var1, var2)