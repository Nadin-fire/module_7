def custom_write(file_name, strings):
    """Записывает в файл file_name все строки strings и возвращает словарь,
    где ключ: (номер строки, байт начала строки), значение: записываемая строка"""
    strings_positions = {}   # Задаем словарь
    number_string = 0
    file = open(file_name, 'a', encoding='utf-8') # Открываем файл для записи с кодировкой utf-8

    for string in strings:
        number_string += 1
        start_str_byte = file.tell() # получаем текущую позиция байта
        strings_positions [(number_string, start_str_byte)] = string # Сохраняем позицию и строку в словарь
        file.write(string + '\n') # Записываем строку в файл с переходом на новую (\n)
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
