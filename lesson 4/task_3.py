a = int(input("Введите натуральное число:"))
a1 = a % 10
a = a // 10
k = 0
while a>0:
   a2 = a % 10
   if a1==a2: k+=1;
   a = a // 10
if k>0: print("Да")
else: print("Нет")