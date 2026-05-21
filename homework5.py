def word_stats(text):
    words = text.split()
    count = len(words)
    unique_words = set(words)
    unique = len(unique_words)
    max_length = len(max(unique_words, key=lambda uw: len(uw)))
    longest = [lw for lw in unique_words if len(lw) == max_length]
    return{
        "count": count,
        "longest": longest,
        "unique": unique
    }


text = "the quick brown fox jumps over the lazy dog"
result = word_stats(text)
print(f"Всего слов: {result['count']}")
print("Слова с макс. кол-вом букв: " + ", ".join(i for i in result['longest']))
print(f"Уникальных: {result['unique']}")