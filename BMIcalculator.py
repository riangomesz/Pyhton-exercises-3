
peso = int(input())
altura = float(input())

imc = peso/altura**2

if imc < 18.5:
   print("Underweight")
elif imc >= 18.5 and imc < 25:
   print("Normal")
elif imc >= 25 and imc < 30:
   print("Overweight")
else:
   print("Obesity")