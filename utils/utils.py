def filter_words(words, user_words):
    return [word for word in words if word['english'] in user_words]