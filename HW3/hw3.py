import os
import csv
import random
import time
import math
def prob1(string1):
    vowelCount = 0
    string1 = string1.lower()
    vowel = set("aeiou")

    for i in string1:
        if i in vowel:
            vowelCount = vowelCount + 1

    if vowelCount > len(string1)/2:
        return True
    elif vowelCount < len(string1)/2:
        return False
    else:
        return None

def prob2(r,h):
    r = r*r
    h = int(math.pi) * h
    return r*h
def prob3():
    x = input("How many strings do you want to join together?: ")
    x = int(x)
    myList = []
    for i in range(x):
        str = input(f"String {i+1} : ")
        myList.append(str)
    print("All strings connected: ",", ".join(myList))
def prob4():
    matrix = []
    letters = ["a","b","c","d","e","f","g"]
    for i in range(5):
        matrix.append([])
        for j in range(5):
            matrix[i].append(random.choice(letters))
    f = open("hw3.txt","w")
    for i in range(5):
        f.write(", ".join(matrix[i]))
        f.write("\n")
    f.close()
    f = open("hw3.txt","r")
    print("Problem 4 using a text file: ",f.read())
    f.close()
def prob4csv():
    matrix = []
    letters = ["a","b","c","d","e","f","g"]
    filename = "hw3.csv"
    for i in range(5):
        matrix.append([])
        for j in range(5):
            matrix[i].append(random.choice(letters))
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(matrix)
    print("Problem 4: CSV file created to store lists")
        
def prob5():
    with open("hw3.csv", newline="\n") as f:
        reader = csv.reader(f)
        data = list(reader)
    print("Problem 5 read from CSV: ",data)
def prob6(x,y):
    try:
        print(f"Solution: {x}/{y}= ",x/y)
    except ZeroDivisionError:
        print("You can't divide by 0 bro")

def prob7():
    list7 = []
    for i in range(20):
        list7.append(random.randint(0,9))
    print("The original list for problem 7: "+ str(list7))
    list7 = list(set(list7))
    print("The list with duplicated removed: " + str(list7))
    
def prob8():
    prob8path = r"C:\Users\antho\Documents\GitHub\Software-Engineering\HW3\hw3-folder"
    if not os.path.exists(prob8path):
        os.makedirs(prob8path)
    print("Problem 8 path created")
    
string1 = input("PLease Enter a String: ")
print(prob1(string1))
print("Ok so lets start to find the volume of a cylider. Please enter the values for the radius and height of the cylinder to get started")
radius = input("Radius: ")
height = input("Height: ")
print("Volume = pi * Height * Radius^2 = ", prob2(int(radius),int(height)))
prob3()
time.sleep(1)
print("\n")
prob4()
prob4csv()
prob5()
print("for problem 6, please enter two numbers. The first number will be divide by the second")
x6 = int(input("First Number: "))
y6 = int(input("Second Number: "))
prob6(x6,y6)
prob7()
prob8()
