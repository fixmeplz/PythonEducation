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
      return "�� ��� ����� ����� �����?"
def integer_division (a,b):
  try:
    return a//b
  except ZeroDivisionError:
    return "�� �� �������..."

print("�������� ��������")
print("1.��������")
print("2.���������")
print("3.���������")
print("4.�������")
print("5.������������� �������")

choice = input("�������� �������: 1, 2, 3, 4, 5:")
num1 = int(input("������� ������ �����:"))
num2 = int(input("������� ������ �����:"))

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
  print("������������ ����")