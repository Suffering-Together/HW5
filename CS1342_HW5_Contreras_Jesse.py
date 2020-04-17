"""
Your Name/s : Jesse Contreras and Damini Gopal
Serial Number/s : 22, 33
Course / Section Number : CS1342 / 251
Homework Number 5
Due Date : April 20 ,2020
"""

def main():
    '''Main algorithm for program that calls other functions throughout.'''
    print("Opportunities to practice functions in Python by Jesse Contreras and Damini Gopal\n")
    firstNum = int(input("Enter The First Number : "))      #int input of inclusive lower bound for range
    print()
    secondNum = int(input("Enter The Second Number : "))    #int input of inclusive upper bound for range
    print("\n\nYou entered :",firstNum,"and",secondNum,"\n")

    if(firstNum < secondNum):
        if(firstNum > -1):
            display_evens(firstNum, secondNum)
            display_odds(firstNum, secondNum)
            print("3. Sum Of All Even Numbers :",sum_evens(firstNum, secondNum))
            print("4. Sum Of All Odd Numbers :",sum_odds(firstNum, secondNum))
            display_primes(firstNum, secondNum)
            display_ints_cubes(firstNum, secondNum)
        else: print("\n\nError : First Number Must Be < Second Number.")
    else: print("\n\nError - Invalid Number : Numbers must be Positive.")

def display_evens(minimum, maximum):
    'Accepts firstNum and secondNum to display all even ints between them.'
    evens = []  #list of even ints
    while (minimum < maximum+1):
        if(minimum %2 ==0): evens.append(minimum)   #if even add to list
        minimum += 1
    print("1. All Even Numbers : ", ','.join(list(map(str, evens))))

def display_odds(minimum, maximum):
    'Accepts firstNum and secondNum to display all odd numbers between them.'
    odds = []   #list of odd ints
    while (minimum < maximum+1):
        if(minimum % 2 == 1): odds.append(minimum)  #if odd add to list
        minimum += 1
    print("2. All Odd Numbers : ", ','.join(list(map(str, odds))))

def sum_evens(minimum, maximum):
    'Accepts firstNum and secondNum to return the sum of all even numbers between them.'
    sum_evens = 0 #int to track the subtotal of all odd numbers
    while (minimum != maximum+1):
        if(minimum%2==0): sum_evens += minimum  #if even add to total
        minimum += 1
    return(sum_evens)

def sum_odds(minimum, maximum):
    'Accepts firstNum and secondNum to return the sum of all even numbers between them.'
    sum_odds = 0
    while (minimum != maximum+1):
        if(minimum%2==1): sum_odds += minimum   #if odd add to total
        minimum += 1
    return(sum_odds)

def display_primes(minimum, maximum):
    'Accepts firstNum and secondNum to display all prime numbers between them.'
    primes = [] #list of ints for prime numbers
    while(minimum < maximum+1):
        if (minimum > 1):
            primes.append(minimum)
        divisor = 2     #int that acts like a divisor for prime prospects
        while(divisor < (minimum//2+1)):
            if (minimum % divisor == 0):
                primes.remove(minimum)  #if divisible by divisor remove number from primes
                break
            divisor += 1
        minimum += 1
    print("5. All Prime Numbers: ", ','.join(list(map(str, primes))))

def display_ints_cubes(minimum, maximum):
    'Accepts firstNum and secondNum to display all ints and between them and their cubes.'
    print("6. Number    Cubed")
    while(minimum < maximum+1):
        print("\n     "+ str(minimum).ljust(9) + str(minimum**3))
        minimum += 1

#Calls main function
main()
