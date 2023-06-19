def is_palindrome(word):
    for i in range(len(word)):
        if word[i] != word[-i-1]:
            return False
    return True

# Пример использования функции
print(is_palindrome("лепсспел"))  # Вывод: True
print(is_palindrome("helloworld"))  # Вывод: False


