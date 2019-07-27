def add(a,b):
  return a+b
def subtract(a,b):
  return a-b
def multiply(a,b):
  return a*b
def divide(a,b):
  try:
      return a/b
  except ZeroDivisionError:
      return "Ты что самый умный здесь?"
def integer_division (a,b):
  try:
    return a//b
  except ZeroDivisionError:
    return "Ну ты Кодзима..."

print("Выберите операцию")
print("1.Сложение")
print("2.Вычитание")
print("3.Умножение")
print("4.Деление")
print("5.Целочилсенное деление")

choice = input("Выберите опрацию: 1, 2, 3, 4, 5:")
num1 = int(input("Введите первое число:"))
num2 = int(input("Введите второе чилсо:"))

if choice == '1':
  print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
  print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
  print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
  print(num1,"/",num2,"=", divide(num1,num2))

elif choice == '5':
  print(num1,"//",num2,"=", integer_division(num1,num2))
else:
  print("Неправильный ввод")