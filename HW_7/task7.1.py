def check_the_phrase(phrase):
    return len(list(filter(lambda letter: letter in ["а", "у", "и", "ы", "о", "э", "ю", "я", "е", "ё"], phrase)))


def check_the_song(func, song):
    return len(set(map(func, song.split())))


song = "пара-ру-рам рым-пам-папам па-ра-па-д "
if check_the_song(check_the_phrase, song) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")