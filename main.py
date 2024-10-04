# Определяем русский алфавит, который будет использоваться для шифрования и дешифрования
alphabet = "абвгдежзийклмнопрстуфхцчшщьыъэюя"

def mod_inverse(a, m):
    """
    Находит обратное по модулю значение a относительно m.

    @param a: Целое число, для которого ищется обратное значение.
    @param m: Модуль.
    @return: Обратное значение x такое, что (a * x) % m = 1, или None, если обратного значения не существует.
    """
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_decrypt(ciphertext, a, b):
    """
    Дешифрует зашифрованный текст методом афинного шифра.

    @param ciphertext: Зашифрованный текст (строка).
    @param a: Параметр шифрования a (целое число).
    @param b: Параметр шифрования b (целое число).
    @return: Дешифрованный текст (строка) или None, если a не имеет обратного по модулю.
    """
    m = len(alphabet)  # Длина алфавита
    a_inv = mod_inverse(a, m)  # Находим обратное значение a

    if a_inv is None:
        return None

    decrypted_text = ""  # Инициализируем переменную для расшифрованного текста

    for char in ciphertext:
        if char in alphabet:
            y = alphabet.index(char)  # Индекс символа в алфавите
            x = (a_inv * (y - b)) % m  # Дешифруем символ
            decrypted_text += alphabet[x]  # Добавляем расшифрованный символ
        else:
            decrypted_text += char  # Если символ не в алфавите, добавляем его как есть

    return decrypted_text

def matches_criteria(decrypted_text, ciphertext, criteria):
    """
    Проверяет соответствие расшифрованного текста заданным критериям.

    @param decrypted_text: Расшифрованный текст (строка).
    @param ciphertext: Исходный зашифрованный текст (строка).
    @param criteria: Словарь с соответствиями букв (dict).
    @return: True, если расшифрованный текст соответствует всем критериям, иначе False.
    """
    for key, valid_letters in criteria.items():
        if key in ciphertext:
            # Проверяем, есть ли в расшифрованном тексте допустимые буквы
            if not any(decrypted_text[i] in valid_letters for i in range(len(decrypted_text)) if ciphertext[i] == key):
                return False
    return True

def brute_force_affine_decrypt(ciphertext):
    """
    Перебирает все возможные ключи для дешифровки.

    @param ciphertext: Зашифрованный текст (строка).
    Выводит: Подходящие ключи и расшифрованный текст, если они найдены.
    """
    m = len(alphabet)  # Длина алфавита

    # Определяем критерии соответствий для проверки расшифровки
    criteria = {
        'к': 'ое',  # Ожидаем, что 'к' может соответствовать 'о' или 'е'
        'л': 'ое',  # Ожидаем, что 'л' может соответствовать 'о' или 'е'
        # Можно добавлять больше соответствий
    }

    for a in range(1, m):
        if mod_inverse(a, m) is not None:  # Проверяем, что a имеет обратное
            for b in range(m):
                decrypted_text = affine_decrypt(ciphertext, a, b)  # Дешифруем текст
                if decrypted_text is not None and matches_criteria(decrypted_text, ciphertext, criteria):
                    # Если текст соответствует критериям, выводим результат
                    print(f"Ключи (a={a}, b={b}): {decrypted_text}")

# Пример использования функции
ciphertext = "бцияхъпаххъпкцмлчлпежмьктлжцднрльклзнэияхиглякцяльгксняжмкгицияпкхмрлглжшлцктажбглыкйнслйихажмциягайль"
brute_force_affine_decrypt(ciphertext)
