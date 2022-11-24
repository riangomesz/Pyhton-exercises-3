# Programa 

a = int(input("Enter a number: "))
print("The prime numbers found are")
for num in range (a):
    div = 0
    for x in range(1,num+1):
        resto = num % x
        if resto == 0:
            div += 1
    if div == 2:
        print(num)
