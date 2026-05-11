# Задача 2: Фильтрация массива строк с помощью лямбда-функций
from typing import Callable, List
import re

def filter_strings(filter_func: Callable[[str], bool], strings: List[str]) -> List[str]:
    # фильтрует массив строк согласно лямбда-функции
    # входные параметры: strings - строки для фильтрации
    # filter_func - функция фильтрации, возвращает значение типа bool
    # возвращаем отфильтрованные строки
        
        return [s for s in strings if filter_func(s)]


def main():
    # тестируем
    test_strings = [
        "hello world",
        "dog",
        "cat",
        "amazing",
        "awful",
        "python",
        "c++"
        "a",
        "   ",
        "long string with spaces",
        "long_string_without_spaces",
        "кит",
        "12345",
        "a good person"
    ]
    
    print("Исходный массив строк:")
    for i, s in enumerate(test_strings, 1):
        print(f"  {i}. '{s}'")
    
    # Фильтр 1: Исключить строки с пробелами
    print("\n" + "="*60)
    print("1. Исключены строки с пробелами:")
    no_spaces_filter = lambda s: ' ' not in s
    result1 = filter_strings(no_spaces_filter, test_strings)
    for s in result1:
        print(f"  '{s}'")
    
    # Фильтр 2: Исключить строки, начинающиеся с буквы "a" (не зависит от регистра и алфавита)
    print("\n" + "="*60)
    print("2. Исключены строки, начинающиеся с буквы 'a':")
    not_start_with_a = lambda s: not s.lower().startswith('a') or s.lower().startswith('а')
    result2 = filter_strings(not_start_with_a, test_strings)
    for s in result2:
        print(f"  '{s}'")
    
    # Фильтр 3: Исключить строки, длина которых меньше 5
    print("\n" + "="*60)
    print("3. Исключены строки, длина которых меньше 5:")
    length_ge_5 = lambda s: len(s) >= 5
    result3 = filter_strings(length_ge_5, test_strings)
    for s in result3:
        print(f"  '{s}'")
    
    # Комбинация фильтров
    print("\n" + "="*60)
    print("Исключены строки короче 5 И начинающиеся не с 'a':")
    combined_filter = lambda s: len(s) >= 5 and not s.lower().startswith('a')
    result4 = filter_strings(combined_filter, test_strings)
    for s in result4:
        print(f"  '{s}'")


if __name__ == "__main__":
    main()