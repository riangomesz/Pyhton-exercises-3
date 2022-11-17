# Program to calculate the BMI of the person and returns to him saying if he is Underweight, Normal, Overweight or Obese

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
