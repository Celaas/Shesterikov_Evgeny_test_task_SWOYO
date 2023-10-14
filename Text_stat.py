"""
Статистика текста
Необходимо разработать функцию text_stat(filename), которая по заданному имени файла
рассчитывала статистику его содержимого. Статистика должна рассчитываться для следующих
категорий:
• Частота использования каждой буквы латинского или кириллического алфавита
• Количество слов в тексте
• Количество абзацев в тексте
• Доля слов, в которых встречается конкретная буква. Если буква встречается в слове более
одного раза, считать это одним попаданием буквы в слово
• Количество слов, в которых одновременно встречаются буквы обоих алфавитов
"""


def text_stat(filename):
    def language(litera):  # внутренняя функция для проверки на то, что буква приндлежит русскому алфавиту
        alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
        return not alphabet.isdisjoint(litera)

    try:
        f = open(filename, 'r', encoding='utf-8')
    except FileNotFoundError:
        return {'error': f'Невозможно открыть файл {filename}, проверьте имя файла и его полный путь'}
    except PermissionError:
        return {'error': 'недомтаточно прав доступа для открытия файла'}
    except IsADirectoryError:
        return {'error': 'ожидался файл, но это директория'}

    # Считаем количество абзацев,за новый абзац принимем выражение \n\t
    paragraph = f.read().split("\n\t")
    paragraph_amount = len(paragraph)
    paragraph = ' '.join(paragraph).split("\n")

    # Считаем количество слов,за слово считаем отделенный пробелом объект состоящий из букв, удаляем сиволы не являющиеся буквами
    text = ' '.join(paragraph)
    text_litera = ''

    for i in range(len(text)):
        if text[i].isalpha() or text[i] == ' ':
            text_litera += text[i]

    l = text_litera.lower().split()
    print(l)
    word_amount = len(l)

    # Считаем слова включающие в себя буквы на разных языках
    bilingual_word_amount = 0
    ru_litera = 0
    en_litera = 0

    for i in range(word_amount):
        for j in range(len(l[i])):
            if language(l[i][j]):
                ru_litera = 1
            else:
                en_litera = 1
        if ru_litera == en_litera:
            bilingual_word_amount += 1
        ru_litera = 0
        en_litera = 0

    # Создаем словарь с известными нам данными
    stat_dict = {
        'word_amount': word_amount,
        'paragraph_amount': paragraph_amount,
        'bilingual_word_amount': bilingual_word_amount
    }

    # Заполняем словарь буквами встречающимися в тексте
    for i in range(word_amount):
        for j in range(len(l[i])):
            share = 0
            quantity = 0
            if stat_dict.get(l[i][j]) == None and l[i][j].isalpha():
                for k in range(word_amount):
                    quantity += l[k].count(l[i][j])
                    word = set(l[k])

                    if not word.isdisjoint(l[i][j]):
                        share += 1

                stat_dict.update({l[i][j]: (quantity, share / word_amount)})

    f.close()

    return stat_dict


text_stat('filename.txt')
