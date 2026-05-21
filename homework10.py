import re
from collections import Counter

def text_analyzer(text):
    """
    Анализирует текст

    Args:
        text (str): входной текст для анализа
    
    Returns:
        dict: словарь со статистикой текста
    """

    # Создаем список слов в нижнем регистре без знаков препинания
    raw_words = re.findall(r'[a-zA-Z]+(?:-[a-zA-Z]+)*', text)
    final_words = [raw_word.lower() for raw_word in raw_words]

    # Средняя длина слова (округлить до 2)
    avg_word_length = round(sum(len(word) for word in final_words) / len(final_words), 2)

    # Топ 3 самых частых слова (список)
    counter = Counter(final_words)
    most_common_words = counter.most_common(3)

    # Создаем список предложений
    raw_sentences = re.split(r'(?<=[.!?])\s+', text)

    # Определяем самое длинное предложение
    longest_sentence = ""
    max_words_count = 0
    for raw_sentence in raw_sentences:
        words = re.findall(r'[a-zA-Z]+(?:-[a-zA-Z]+)*', raw_sentence)
        if len(words) > max_words_count:
            max_words_count = len(words)
            longest_sentence = raw_sentence

    # Возвращаем результат
    return {
        "words": len(final_words), # Количество слов
        "sentences": len(raw_sentences),# количество предложений
        "avg_word_length": avg_word_length,  # cредняя длина слова (округлить до 2)
        "most_common_words": most_common_words,  # топ 3 самых частых слова (список)
        "longest_sentence": longest_sentence # самое длинное предложение (по количеству слов)
    }

text = "Python is great. Python is easy to learn. Everyone should learn Python. It is the best language."
print(text_analyzer(text))
