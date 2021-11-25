getName = input("Введите своё имя: ")

for letter in getName:

   getName = getName.replace(letter, "*")

print("\nРезультат:", getName)
