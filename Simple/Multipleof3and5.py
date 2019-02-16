'''
Problem Statement : 
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

def isMultipleof3or5(x):
    if x%3 == 0 or x%5 ==0:
        return True
    else:
        return False


def calculateSumofMutlipleof3or5(number_range):
    total=0
    for num in range(1,number_range):
        if isMultipleof3or5(num):
            total += num
    
    print("Input Range :: {} , Total Sum : {}".format(number_range,total))


calculateSumofMutlipleof3or5(10)
calculateSumofMutlipleof3or5(20)