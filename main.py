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