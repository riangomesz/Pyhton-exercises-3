a = int(input('Type the first number: ' ))
b = int(input('Type the second number: ' ))

soma = lambda a, b: a + b
sub =  lambda a, b: a - b
mult = lambda a, b: a * b
divi = lambda a,b: a / b

print('The sum is: ' + str(soma(a,b)))
print('The subtraction is: ' + str(sub(a,b)))
print('The multiplication is: '+ str(mult(a,b)))
print('The division is: '+ str(divi(a,b)))

calculator = {
    'sum': lambda a,b: a + b,
    'sub': lambda a,b: a - b,
    'mult': lambda a,b: a * b,
    'divi': lambda a,b: a / b,
}
print(type(calculator))
soma = lambda a,b: a + b,
mult = calculator['mult']
