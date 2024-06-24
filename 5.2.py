# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, 
# print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and 
# put out an appropriate message and ignore the number. Enter 7, 2, bob, 1None, and 4 and match the output below

small_num = None
large_num = None

def findLargestNum(inum):
    global large_num
    if large_num == None or large_num < inum :
        large_num = inum
    return large_num

def findSmallestNum(inum):
    global small_num
    if small_num == None or small_num > inum:
        small_num = inum
    return small_num

while True:
    snum = input("Enter a number:")
    if snum == 'done':
        if large_num != None or small_num != None:
            print("all Done")
            print("Smallest Number is :", smallestNum)
            print("Largest Number is :", largestNum)
            break
        else : 
            print("You have not entered any input values.")
            continue
    try:
        inum = int(snum)
    except:
        print("Invalid Input")
        continue
    smallestNum = findSmallestNum(inum)
    largestNum = findLargestNum(inum)