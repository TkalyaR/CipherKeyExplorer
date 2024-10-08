# Определяем русский алфавит, который будет использоваться для шифрования и дешифрования
import argparse


def ex_gcd(a, b, x=0, y=1):
    """
    Вычисляет наибольший общий делитель (НОД) двух чисел a и b
    с использованием расширенного алгоритма Евклида. Также возвращает
    коэффициенты x и y такие, что ax + by = gcd(a, b).

    :param a: Первое число (целое), для которого вычисляется НОД.
    :param b: Второе число (целое), для которого вычисляется НОД.
    :param x: Переменная для хранения коэффициента x в уравнении ax + by = gcd(a, b).
    :param y: Переменная для хранения коэффициента y в уравнении ax + by = gcd(a, b).
    :return: Кортеж (d, x, y), где d - НОД(a, b), x и y - коэффициенты, удовлетворяющие уравнению.
    """
    if a == 0:
        return abs(b), 0, 1
    d, x1, y1 = ex_gcd(b % a, a, x, y)
    x = y1 - (b // a) * x1
    return d, x, x1


def mod_inverse(a, m):
    """
    Находит обратное по модулю значение a относительно m.

    :param a: Целое число, для которого ищется обратное значение.
    :param m: Модуль.
    :return: Обратное значение x такое, что (a * x) % m = 1, или None, если обратного значения не существует.
    """
    if m <= 0:
        raise ValueError("Модуль должен быть больше 0.")
    a = a % m  # Приводим a к положительному значению в пределах [0, m)

    g, x, _ = ex_gcd(a, m)
    if g != 1:
        return None  # Обратного элемента не существует
    return x % m


def affine_decrypt(ciphertext, a, b, alphabet):
    """
    Дешифрует зашифрованный текст методом афинного шифра.

    :param ciphertext: Зашифрованный текст (строка).
    :param a: Параметр шифрования a (целое число).
    :param b: Параметр шифрования b (целое число).
    :return: Дешифрованный текст (строка) или None, если a не имеет обратного по модулю.
    """
    m = len(alphabet)  # Длина алфавита
    a_inv = mod_inverse(a, m)  # Находим обратное значение a

    if a_inv is None:
        return None

    # Расшифровываем текст
    decrypted_text = ""  # переменная для расшифрованного текста
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
    Проверяет, соответствует ли расшифрованный текст заданным критериям.

    :param decrypted_text: Расшифрованный текст.
    :param ciphertext: Исходный зашифрованный текст.
    :param criteria: Словарь с соответствиями букв (dict).
    :return: True, если расшифрованный текст соответствует всем критериям, иначе False.
    """
    for key, valid_letters in criteria.items():
        if key in ciphertext:
            # Проверяем, есть ли в расшифрованном тексте допустимые буквы
            if not any(decrypted_text[i] in valid_letters for i in range(len(decrypted_text)) if ciphertext[i] == key):
                return False
    return True


def most_frequent_letters(text, n=5):
    """
    Находит самые популярные буквы в строке.

    :param text: Исходная строка.
    :param n: Количество самых популярных букв для возврата.
    :return: Список кортежей с n символами по частоте повторений.
    """
    frequency = {}  # Переменная для подсчета частоты букв
    for char in text:
        if char.isalpha():  # Убедимся, что это буква
            frequency[char] = frequency.get(char, 0) + 1  # Увеличиваем счетчик

    # Сортируем буквы по частоте и возвращаем N-букв
    sorted_letters = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
    return sorted_letters[:n]


def brute_force_affine_decrypt(ciphertext, depth=2, width=4, language='ru'):
    """
    Перебирает все возможные ключи для дешифровки.

    :param language: язык
    :param ciphertext: Зашифрованный текст (строка).
    :param depth: Глубина поиска (количество совпадений).
    :param width: Ширина поиска (количество критериев).
    """

    if width < depth:
        raise ValueError("Error: the search depth cannot be less than the width")
    if depth < 2:
        raise ValueError("Error: the depth cannot be less than 2")

    alphabet = {
        'ru': 'абвгдежзийклмнопрстуфхцчшщьыъэюя',
        'en': 'abcdefghijklmnopqrstuvwxyz',
    }
    m = len(alphabet[language])  # Длина алфавита

    # Поиск совпадений
    top = most_frequent_letters(ciphertext, depth)
    top_char = {
        'ru': 'оеаинтсрвлкмдпуяыьгзбчйхжшюцщэфёъ',
        'en': 'edsarntolcudpmghbyfvkwzxqj',
    }
    permutation = ''
    for i in range(width):
        permutation += top_char[language][i]

    # Определяем критерии соответствий для проверки расшифровки
    criteria = {}
    for char, _ in top:
        criteria[char] = permutation
    print(criteria)

    for a in range(1, m):
        if mod_inverse(a, m) is not None:  # Проверяем, что a имеет обратное
            for b in range(m):
                decrypted_text = affine_decrypt(ciphertext, a, b, alphabet[language])  # Дешифруем текст
                if decrypted_text is not None and matches_criteria(decrypted_text, ciphertext, criteria):
                    # Если текст соответствует критериям, выводим результат
                    print(f"a={a}, b={b}\t->\t{decrypted_text}")


def main():
    parser = argparse.ArgumentParser(description='CipherKeyExplorer')
    parser.add_argument('-i', '--input', type=str, required=True, help='Ciphertext string to be decrypted.')
    parser.add_argument('-d', '--depth', default=2, type=int, help='Search depth for matching criteria (minimum 2).')
    parser.add_argument('-w', '--width', default=3, type=int, help='Search width for matching criteria (minimum 2).')
    parser.add_argument('-l', '--language', type=str, choices=['ru', 'en'], default='ru',
                        help='Substitution language (default: ru). Choices: ru, en')
    args = parser.parse_args()

    ciphertext = args.input
    deep = args.depth
    width = args.width
    language = args.language

    brute_force_affine_decrypt(ciphertext, deep, width, language)


if __name__ == '__main__':
    main()
