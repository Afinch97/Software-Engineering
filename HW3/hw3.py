#import pandas as pd
import csv
import random
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
    h = 3.14 * h
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
    print(f.read())
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

def prob5():
    with open("hw3.csv", newline="\n") as f:
        reader = csv.reader(f)
        data = list(reader)
    print(data)


#string1 = input("PLease Enter a String: ")
#print(prob1(string1))
#print("Ok so lets start to find the volume of a cylider. Please enter the values for the radius and height of the cylinder to get started")
#radius = input("Radius: ")
#height = input("Height: ")
#print("Volume = pi * Height * Radius^2 = ", prob2(int(radius),int(height)))
#prob3()
#prob4()
prob4csv()
prob5()
