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


# ЗАВДАННЯ 4.  консольному боту-помічнику додати обробку помилок за допомоги декораторів

# додаємо декоратор для обробки помилок
def input_error(func):
    def inner(*args, **kwargs):
        function_name = str(func).split(" ")[1]
        try:
            return func(*args, **kwargs)
        # якщо помилка при введенні команди add
        except ValueError:
            if function_name == "parse_input":
                return  f"Неправильно введена команда.\
                    \nПотрібно ввести ім'я та номер телефону."
            elif function_name == "add_contact":
                return  f"Неправильно введена команда.\
                    \nПотрібно ввести ім'я та номер телефону."
            elif function_name == "change_phone":
                return  f"Неправильно введена команда.\
                    \nПотрібно ввести ім'я та новий номер телефону."
            elif function_name == "name_out":
                return  f"Контакту не існує. Потрібно додати такий номер телефону.\n"
            
        # навіщо нам IndexError  якщо маємо словник, а не список ???
        except IndexError:
            if function_name == "show_phone":
                return f"Неправильно введена команда.\
                    \nПотрібно ввести phone name"
        
        # виводить помилку, якщо немає такого контакту       
        except KeyError:                                   
                   if function_name == "show_phone":
                return f"Контакту не існує. Потрібно додати такий номер телефону.\n"
  
    return inner


@input_error
# функція взаємодії з користувачем
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
# функція виводу іʼмя у відповідях боту
def name_out(name:str):
    return f"{name}"

# функція виводу номеру телефону за імʼям контакту
@input_error
def show_phone(args, contacts):
    name=args[0]
    if name in contacts:
        return f"Телефон контакту {name_out(name)} є {contacts[name]}"
 
# функція додавання контактів
@input_error
def add_contact(args, contacts):
    name, phone = args
    if phone.isdigit():
        # перевіряємо чи вже існує такий номер
        if phone in contacts.values():
            return "Цей номер вже присутній у контактах."
        # перевіряємо чи вже існує таке ім'я
        elif name in contacts.keys():               
            return f"Контакт {name_out(name)} вже існує."
        # якщо все правильно додаємо контакт
        else:
            contacts[name] = phone
            return f"Контакт {name_out(name)} додано."
    else:
        return "Номер не є цифрами."


# функція виводу всіх контактів    
@input_error
def all_contacts(contacts):
    if contacts == {}:
        return "Warning: Contacts list is empty."
    else:
        return f"{contacts}"


# функція зміни номеру у словнику
@input_error
def change_phone(args, contacts):
    name, new_phone = args
    # перевіряємо чи новий телефон скдадається з цифр
    if not new_phone.isdigit():
        return  "Новий номер телефону повинен містити лише цифри."
    # перевіряємо чи існує такий контакт
    if name not in contacts:
        return f"Попередження: Контакт {name_out(name)} не знайдено."
    
    contacts[name] = new_phone
    return f"Номер телефону контакту {name_out(name)} змінено на {new_phone}"
    

# головна функція
def main():
    contacts = {}
    
    while True:      

        user_input = input(f"Введіть команду: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command in ["hello", "привіт"]:
            print("Як я можу вам допомогти?")

        elif command in ["add", "додати"]:
            print(add_contact(args, contacts))
            
        elif command == "phone":
            print(show_phone(args, contacts))           
            
        elif command == "all":
            print(f"{all_contacts(contacts)}")
        
        elif command == "change":
            print(change_phone(args, contacts))
        
        else:
            print("Невірна команда. Спробуйте ще")

if __name__ == "__main__":
    main()