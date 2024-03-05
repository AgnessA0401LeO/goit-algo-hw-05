# ФУНКЦІЯ caching_fibonacci
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
# Приклад використання
fib = caching_fibonacci()

print(fib(15))
print(fib(10))