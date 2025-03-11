# Функція для обчислення z
def calczi(m):
    return (m ** 0.5) + 10

# Функція для знаходження середнього арифметичного всіх парних чисел від x до y
def avgsimple(x, y):
    suma = 0
    count = 0
    for num in range(x, y + 1):
        if num % 2 == 0:
            suma += num
            count += 1

    # Перевірка чи є парні числа
    if count == 0:
        return 0
    
    return suma / count

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