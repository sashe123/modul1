import math
import json

def can_form_triangle(a, b, c):
    """Перевірка умови існування трикутника."""
    return a + b > c and a + c > b and b + c > a

def area_of_triangle(a, b, c):
    """Обчислення площі трикутника за формулою Герона."""
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def fib(k):
    """Рекурсивна функція для обчислення числа Фібоначчі."""
    if k < 0:
        raise ValueError("Індекс не може бути від'ємним")
    elif k == 0:
        return 0
    elif k == 1:
        return 1
    else:
        return fib(k - 1) + fib(k - 2)

def main():
    # Введення сторін трикутників
    try:
        a1, b1, c1 = map(float, input("Введіть величини сторін першого трикутника (a1, b1, c1): ").split(','))
        a2, b2, c2 = map(float, input("Введіть величини сторін другого трикутника (a2, b2, c2): ").split(','))
        language = input("Введіть мову інтерфейсу (uk/en): ")
    except ValueError:
        print("Некоректні дані, спробуйте ще раз.")
        return

    # Перевірка можливості існування трикутників
    if not (can_form_triangle(a1, b1, c1) and can_form_triangle(a2, b2, c2)):
        print("Один або обидва трикутники не можуть існувати.")
        return
    
    # Обчислення площ
    area1 = area_of_triangle(a1, b1, c1)
    area2 = area_of_triangle(a2, b2, c2)

    # Виведення результатів
    if language.lower() == 'uk':
        print(f"Площа першого трикутника: {area1:.2f}")
        print(f"Площа другого трикутника: {area2:.2f}")
        
        if area1 > area2:
            print("Площа першого трикутника більше другого.")
        elif area2 > area1:
            print("Площа другого трикутника більше першого.")
        else:
            print("Площі трикутників рівні.")
        
        # Збереження даних у файл
        data = {
            "triangle_1": {"sides": (a1, b1, c1), "area": area1},
            "triangle_2": {"sides": (a2, b2, c2), "area": area2},
            "language": language
        }
        with open('MyData.json', 'w') as file:
            json.dump(data, file)
        print("Дані збережено в файл MyData.json")
        
    else:
        print("Unsupported language. Please use 'uk' for Ukrainian.")

    # Введення індексу для обчислення числа Фібоначчі
    k = int(input("Введіть індекс для числа Фібоначчі: "))
    fib_result = fib(k)
    print(f"Число Фібоначчі для k={k} дорівнює {fib_result}")

if __name__ == "__main__":
    main()
