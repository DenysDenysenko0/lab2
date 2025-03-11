from mod import avgsimple

# Функція для обчислення z
def calczi(m):
    return (m ** 0.5) + 10

# Введення значень користувачем
m = int(input("Введіть m: "))
while (m < 0):
    print("m не може бути меншим за 0!")
    m = int(input("Введіть ще раз m: "))

x = int(input("Введіть x: "))
y = int(input("Введіть y: "))

# Виклик функцій і вивід результатів обчислень
print("Результат z = ", calczi(m))

avgnum = avgsimple(x, y)
if avgnum is not 0:
    print("Середнє арифметичне парних чисел = ", avgnum)
else:
    print("Парних чисел не виявлено, середнє арифметичне не можливо порахувати")