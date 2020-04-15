"""




"""
    
def display_evens(minimum, maximum):
    'accepts firstNum and secondNum to display all even ints between them'
    evens = []  #list of even ints
    while (minimum < maximum+1):
        if(minimum %2 ==0): evens.append(minimum)   #if even add to list
        minimum += 1
    print("Even Numbers:", ','.join(list(map(str, evens))))

def display_odds(minimum, maximum):
    'accepts firstNum and secondNum to display all odd numbers between them'
    odds = []   #list of odd ints
    while (minimum < maximum+1):
        if(minimum % 2 == 1): odds.append(minimum)  #if odd add to list
        minimum += 1
    print("Odd Numbers:", ','.join(list(map(str, odds))))

def sum_evens(minimum, maximum):
    'accepts firstNum and secondNum to return the sum of all even numbers between them'
    sum_evens = 0 
    while (minimum != maximum+1):
        if(minimum%2==0): sum_evens += minimum
        minimum += 1
    print("sum of evens:", sum_evens)

def sum_odds(minimum, maximum):
    'accepts firstNum and secondNum to return the sum of all even numbers between them'
    total = 0
    while (minimum != maximum+1):
        if(minimum%2==1):
            total += minimum
        minimum += 1
    return("sum of odds:", total)

def display_primes(minimum, maximum):
    'accepts firstNum and secondNum to display all prime numbers between them'
    primes = []
    while(minimum < maximum+1):
        if (minimum > 1): primes.append(minimum)
        divisor = 2
        while(divisor < (minimum//2+1)):
            if (minimum % divisor == 0):
                primes.remove(minimum)
                break
            divisor += 1
        minimum += 1
    print("Prime Numbers:", ','.join(list(map(str, primes))))

def display_ints_cubes(minimum, maximum):
    'accepts firstNum and secondNum to display all ints and between them and their cubes'
    print("6. Number    Cubed")
    while(minimum < maximum+1):
        print("     "+ str(minimum).ljust(9) + str(minimum**3))
        minimum += 1
    
firstNum = int(input("Enter First Num:"))
secondNum = int(input("Enter Second Num:"))

if(firstNum < secondNum):
    if(firstNum > -1):
        display_evens(firstNum, secondNum)
        display_odds(firstNum, secondNum)
        sum_evens(firstNum, secondNum)
        sum_odds(firstNum, secondNum)
        display_primes(firstNum, secondNum)
        display_ints_cubes(firstNum, secondNum)
    else: print("INVALID NEGATIVE")
else: print("INVALID 1 > 2")
