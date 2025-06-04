

# 1. 
def square_perimeter_and_area(side):
    perimeter = 4 * side
    area = side ** 2
    return perimeter, area

# 2.
def circle_length(diameter):
    length = math.pi * diameter
    return length

# 3. Найти среднее двух чисел
def mean_of_two(a, b):
    return (a + b) / 2

# 4. Найти сумму, произведение и квадрат каждого числа
def calculate_operations(a, b):
    sum_ab = a + b
    product_ab = a * b
    square_a = a ** 2
    square_b = b ** 2
    return sum_ab, product_ab, square_a, square_b

# Ввод данных пользователем
side = float(input("Введите длину стороны квадрата: "))
diameter = float(input("Введите диаметр окружности: "))
a = float(input("Введите первое число (a): "))
b = float(input("Введите второе число (b): "))

# Вычисления и вывод
perimeter, area = square_perimeter_and_area(side)
print(f"\nПериметр квадрата: {perimeter}")
print(f"Площадь квадрата: {area}")

circle_len = circle_length(diameter)
print(f"\nДлина окружности: {circle_len:.2f}")

mean = mean_of_two(a, b)
print(f"\nСреднее значение чисел {a} и {b}: {mean}")

sum_ab, product_ab, square_a, square_b = calculate_operations(a, b)
print(f"\nСумма: {sum_ab}")
print(f"Произведение: {product_ab}")
print(f"Квадрат числа {a}: {square_a}")
print(f"Квадрат числа {b}: {square_b}")
