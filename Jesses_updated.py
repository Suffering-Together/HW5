"""




"""
    
def display_evens(minimum, maximum):
    'accepts firstNum and secondNum to display all even ints between them'
    evens = []  #list of even ints
    while (minimum < maximum+1):
        if(minimum %2 ==0): evens.append(minimum)   #if even add to list
        minimum += 1
    print("1. All Even Numbers : ", ','.join(list(map(str, evens))))

def display_odds(minimum, maximum):
    'accepts firstNum and secondNum to display all odd numbers between them'
    odds = []   #list of odd ints
    while (minimum < maximum+1):
        if(minimum % 2 == 1): odds.append(minimum)  #if odd add to list
        minimum += 1
    print("2. All Odd Numbers : ", ','.join(list(map(str, odds))))

def sum_evens(minimum, maximum):
    'accepts firstNum and secondNum to return the sum of all even numbers between them'
    sum_evens = 0 
    while (minimum != maximum+1):
        if(minimum%2==0): sum_evens += minimum
        minimum += 1
    return(sum_evens)

def sum_odds(minimum, maximum):
    'accepts firstNum and secondNum to return the sum of all even numbers between them'
    sum_odds = 0
    while (minimum != maximum+1):
        if(minimum%2==1): sum_odds += minimum
        minimum += 1
    return(sum_odds)

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
    print("5. AllPrimeNumbers: ", ','.join(list(map(str, primes))))

def display_ints_cubes(minimum, maximum):
    'accepts firstNum and secondNum to display all ints and between them and their cubes'
    print("6. Number    Cubed")
    while(minimum < maximum+1):
        print("     "+ str(minimum).ljust(9) + str(minimum**3))
        minimum += 1
    
print("Opportunities to practice functions in Python by Jesse Contreras and Damini Gopall\n")
firstNum = int(input("Enter The First Number : "))
secondNum = int(input("Enter The Second Number : "))
print("\nYou entered :",firstNum,"and",secondNum,"\n")

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
