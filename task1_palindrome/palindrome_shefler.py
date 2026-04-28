# Задача 1: Проверка является ли строка палиндромом
def is_palindrome(s: str) -> bool:
    # входной параметр s - строка
    # возвращаем true или false (палиндром или нет)
    
    # приводим к нижнему регистру и оставляем только буквы и цифры
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    # сравниваем строку с её перевёрнутой версией
    return cleaned == cleaned[::-1]

def main():
    # тестируем
    test_cases = [
        "Hello, world!",
        "И темен город. Мороз, узором дорог не мети.",
        "12321",
        "A man, a plan, a canal, Panama!",
        "Не палиндром",
        "",
        "m",
    ]
    
    print("Тест:")
    for test in test_cases:
        result = is_palindrome(test)
        print(f"'{test}' - {result}")

if __name__ == "__main__":
    main()