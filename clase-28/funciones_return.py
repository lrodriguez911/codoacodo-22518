def rest(num1, num2):
    res = num1 - num2
    return res
    

def square_of_even(num):
    if num % 2 == 0:
        print(num ** 2)
    else:
        return

def is_even(num):
    return num % 2 == 0


def squared_and_cubed(num):
    return num ** 2, num ** 3


def operations(a, b):
    if b != 0: 
        return a+b, a-b, a*b, a/b
    else:
        return a+b, a-b , a*b, a/b, "Error b is zero"
# main program

suma, resta, multi, div = operations(5, 2)
squared, cubeb =  squared_and_cubed(8)
print(f'Squared: {squared}\nCubed: {cubeb}')



'''print(is_even(4))
print(is_even(4))
for i in range(1, 20):
    if is_even(i):
        print(i, end=' ')

square_of_even(8)
print(square_of_even(3))'''


result = rest(10, 3) # saving the result using in a var
print(f'the result is : {result}') 
print(f'the result is : {rest(5 , 2)}') # just showing the result