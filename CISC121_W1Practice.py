# Week 1 Practice Exercises

# 1. Basic Python
bookTitle = "Harry Potter"
numPages = 200

print("The book %s has %d pages" %(bookTitle, numPages))


#length = int(input("Enter a length : "))
#width = int(input("Enter a width : "))
#area = length*width
#perim = 2*length + 2*width
#print("The area is %d and perimeter is %d" %(area, perim))

# 2. Python Functions & 3. Control Structures
def totalPrice(mealPrice, tipPercent):
    if tipPercent < 10:
        print("Cheapskate")
        return -1
    if 10 < tipPercent < 15:
        print("You can do better than that. How about 20%?")
        totalMealPrice = mealPrice + tipPercent*mealPrice
        return totalMealPrice


def add(a,b):
    sum = a + b
    return sum

def subtract(c,d):
    difference = c - d
    return difference

def happyBday(name):
    print("Happy birthday to " + name)

happyBday('elaine')

def gradeGen(numGrade):
    if 80<=numGrade <=100:
        print("A")
    elif 70<=numGrade<=79:
        print("B")
    elif 60<=numGrade<=69:
        print("C")
    elif 50<=numGrade<=59:
        print("D")
    else: 
        print("F")

gradeGen(25)


# 4. Loops

numbos = [7, 9, 14, 32, 22, 0]
start = 3
end = 5

def listWalk(array, start, end):
    print(numbos[start:end+1]) #end+1 makes it inclusive

listWalk(numbos, start,end)

def printDuplicate(array1, array2):
    for x in range(0,len(array1)):
        for y in range(0,len(array2)):
            if array1[x] == array2[y]:
                print(array1[x]) #print duplicate
                       

printDuplicate([11,2,4], [2,4,5])

def printOther(array):
    for x in range(0, len(array),2):
        print(array[x])

printOther([2,4,5,14,26,47,25])

def printReverse(array):
    for x in range(0, len(array)):
        backwardArray[x] = array[len(array)-1]

    return backwardArray

printReverse([3,34,66,6])            
            
            
    
