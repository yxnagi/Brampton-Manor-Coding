import time


def bruteforce():
    number = int(input(f"Please enter your desired number to compute from 1 - to that number "))
    startTime = time.time()
    sum = 0
    for x in range(1,number):
        sum += x
        print(sum)
    sum += number
    return sum, startTime

def formula():
    number = int(input(f"Please enter your desired number to compute from 1 - to that number "))
    startTime = time.time()
    sum = 0
    sum = ((number**2) + (number)) / 2
    return sum, startTime

sum, startTime = bruteforce()
print(sum)
executionTime = (time.time() - startTime)
print('BRUTE FORCE Execution time in seconds: ' + str(executionTime))
sum, startTime = formula()
print(sum)
executionTime = (time.time() - startTime)
print('FORMULA Execution time in seconds: ' + str(executionTime))