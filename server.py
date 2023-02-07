import statistics
import sys

def checkIntegers(lst):
    return all(i.isdigit() for i in lst)

def Mean(lst):
    return statistics.mean(lst)

def Median(lst):
    return statistics.median(lst)

def Mode(lst):
    return statistics.mode(lst)

print("Server is ready. You can type intergers and then click [ENTER].  Clients will show the mean, median, and mode of the input values.")

inp = input()

if inp == "Q":
    sys.exit()

lst = inp.split()

check = checkIntegers(lst)

if check == False:
    print("Invalid Input!")
else:
    req = list(map(int, lst))

    avg = Mean(req)
    med = Median(req)
    mod = Mode(req)

    print("Mean is ", avg)
    print("Median is ", med)
    print("Mode is ", med)
