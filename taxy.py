import math

def bracketOne(userSalary):
    taxAmount = userSalary * .10
    postTax = userSalary - taxAmount
    print(postTax)

def bracketTwo(userSalary):
    flatRate = 987.50                
    amountOver = userSalary - 9875     
    percentage = amountOver * .12       
    result = flatRate + percentage
    print(result)

def bracketThree(userSalary):
    flatRate = 4617.50
    amountOver = userSalary - 40125
    percentage = amountOver * .22
    result = flatRate + percentage
    print(result)

def bracketFour(userSalary):
    flatRate = 14605.50
    amountOver = userSalary - 85525
    percentage = amountOver * .24
    result = flatRate + percentage
    print(result)

def bracketFive(userSalary):
    flatRate = 33271.50
    amountOver = userSalary - 163300
    percentage = amountOver * .32
    result = flatRate + percentage
    print(result)

def bracketSix(userSalary):
    flatRate = 47367.50
    amountOver = userSalary - 207350
    percentage = amountOver * .35
    result = flatRate + percentage
    print(result)

def bracketSeven(userSalary):
    flatRate = 156235
    amountOver = userSalary - 518400
    percentage = amountOver * .37
    result = flatRate + percentage
    print(result)

userInput = int(input("Enter your salary:\n"))

if userInput < 9875:
    bracketOne(userInput)

if 9876 <= userInput <= 40125:
    bracketTwo(userInput) 

if 40126 <= userInput <= 85525:
    bracketThree(userInput)

if 85526 <= userInput <= 163300:
    bracketFour(userInput)

if 163301 <= userInput <= 207350:
    bracketFive(userInput)

if 207351 <= userInput <= 518400:
    bracketSix(userInput)

if userInput > 518401:
    bracketSeven(userInput)