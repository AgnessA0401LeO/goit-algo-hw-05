# ЗАВДАННЯ 1.ФУНКЦІЯ caching_fibonacci
def caching_fibonacci():
    #     Створити порожній словник cache
    cache = {}
    #     ФУНКЦІЯ fibonacci(n)
    def fibonacci(n):
        # розрахунки функції
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]

    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()
# Приклад використання
print(fib(15))
print(fib(10))


# ЗАВДАННЯ 2. Генератор, який шукає  дійсні числа з тексту та сумумє їх
from typing import Callable
import re
# функція для пошуку дійсних чисел в тексті
def generator_numbers(text: str):
    # створюємо шаблон для пошуку чисел і враховуємо що може бути крапка між цифрами
    pattern = r'\s+\d+\.{0,1}\d*\s+'
    for match in re.finditer(pattern, text):
        yield float(match.group())

# функція для розрахунку суми чисел у тексті
def sum_profit(text: str, func: Callable):
    numbers = func(text)
    total_sum = sum(numbers)
    return total_sum

text = "Загальний дохід працівника  складається or 25 з декількох частин: 1000.01 як основний дохід, \
    доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")