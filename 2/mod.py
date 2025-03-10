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