# Задача 5: Декоратор для замера времени выполнения функции
# Как я поняла екоратор - это функция, которая оборачивает другую функцию и делает что-то до/после её выполнения, иными словами можно добавлять функционал не меняя основную функцию
import time
import os
from typing import Any, Callable

def timer_decorator(func: Callable) -> Callable:
    #Вызывается не исходная функция, а обертка
    #Запоминается время до вызова функции
    #Вызов исходной функции
    #Вычисление разницы и возврат ее как результата
    
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs) 
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        print(f"[ДЕКОРАТОР] Функция '{func.__name__}' выполнялась: {elapsed_time:.6f} секунд")
        
        return result
    
    return wrapper

@timer_decorator
def sum_and_print(a: float, b: float) -> None:
    # суммируем числа из консоли, выводим в консоль
    result = a + b
    print(f"Сумма {a} + {b} = {result}")
    # чтобы было более наглядно делаем time.sleep
    time.sleep(0.1)


@timer_decorator  # применяем тот же декоратор
def process_file() -> None:
    #суммируем числа из файла и выводим в файл
    # определяем текущую папку, а от нее пути
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(current_dir, "input.txt")
    output_path = os.path.join(current_dir, "output.txt")
    
    # Читаем числа из файла
    print(f"Читаем файл: {input_path}")
    
    with open(input_path, 'r', encoding='utf-8') as file:
        content = file.read().strip()
    
    # реализуем считывание вне зависимости от того, как отделены числа
    # если в строке есть пробел - разделяем по пробелу
    if ' ' in content:
        parts = content.split()
    else:
        # если его нет  разделим по переводу строки
        parts = content.split()
    
    # если строк больше двух, берем первые две
    if len(parts) >= 2:
        a = float(parts[0])
        b = float(parts[1])
    else:
        # при ошибке
        raise ValueError(f"Не удалось прочитать два числа из файла: '{content}'")
    
    # считаем сумму
    result = a + b
    
    # записываем результат
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(f'{result}')
    
    print(f"Записали результат в файл: {output_path}")

@timer_decorator
def slow_function() -> None:
    # это специальная функция, которая спит дольше, чтобы посмотреть, что декоратор работает
    print("Долгая функция старт")
    time.sleep(0.3)
    print("Долгая функция стоп")


def main():
    # тестируем
    
    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ДЕКОРАТОРА ЗАМЕРА ВРЕМЕНИ")
    print("=" * 60)
    
    print("\nТест 1: Функция сложения двух чисел")
    sum_and_print(10, 25)
    sum_and_print(3.14, 2.86)
    
    print("\nТест 2: Функция работы с файлами")
    # сначала создадим input.txt, если его нет
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(current_dir, "input.txt")
    
    if not os.path.exists(input_path):
        # Создаем файл с примером данных
        with open(input_path, 'w', encoding='utf-8') as f:
            f.write("67 89")
        print(f"Создан файл input.txt с числами 67 и 89")
    
    process_file()
    
    print("\nТест 3: Долгая функция")
    slow_function()
    
    print("\n" + "=" * 60)
    print("конец тестов")
    print("=" * 60)


if __name__ == "__main__":
    main()