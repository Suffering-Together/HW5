first_num = int()
second_num = int()
format_string = str()
total = int()
is_prime = bool()
divisor = int()

def evens(counter,end):
    format_string = ""
    while(counter != end+1):
        if (counter %2 == 0): format_string += str(counter) + ","
        counter += 1
    print(format_string[:len(format_string)-1])

def odds(counter,end):
    format_string = ""
    while(counter != end+1):
        if (counter%2==1): format_string += str(counter) + ","
        counter += 1
    print(format_string[:len(format_string)-1])

def sum_evens(counter,end):
    total = 0
    while(counter != end+1):
        if(counter%2==0): total += counter
        counter += 1
    print(total)

def sum_odds(counter,end):
    total = 0
    while(counter != end+1):
        if(counter%2==1): total += counter
        counter += 1
    print(total)

def primes(counter,end):
    format_string = ""

    while(counter != end+1):
        divisor = 2
        is_prime = True
        
        while(divisor < counter):            
            if(counter % divisor == 0): is_prime = False
            divisor += 1

        if (counter == 0 or counter == 1): is_prime = False    
        if (is_prime): format_string += str(counter) + ","
        counter += 1
        
    print(format_string[:len(format_string)-1])

def ints_cubed(minimum, maximum):
    while(minimum < maximum+1):
        print(minimum, minimum**3)
        minimum += 1
    

first_num = int(input("Enter min:"))
second_num = int(input("Enter max:"))

evens(first_num, second_num)
odds(first_num, second_num)
sum_evens(first_num, second_num)
sum_odds(first_num, second_num)
primes(first_num, second_num)
ints_cubed(first_num, second_num)
