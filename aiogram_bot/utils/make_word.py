"""A module for searching for words in the dictionary."""

import pathlib

PATH_FILE = pathlib.Path(__file__).parent.resolve()
FILE_NAME = "russian_nouns.txt"

with open(PATH_FILE.joinpath(FILE_NAME), "r", encoding="utf-8") as file:
    LIST_WORDS = file.read().lower().split()


async def find_words(user_word: str) -> dict[int:list[str]]:
    """
    The find_words function. Finds words from symbols in the dictionary.
    """
    user_word_split = list(user_word)
    for ind, sym in enumerate(user_word):
        if ord(sym) == 235:
            user_word_split[ind] = "ё"

    user_word = "".join(user_word_split)
    result_words = []
    dict_count_letter = {sym: user_word.count(sym) for sym in user_word}
    for word in LIST_WORDS:
        if all(sym in user_word for sym in word):
            list_true = []
            for sym in word:
                count_letter = word.count(sym)
                if dict_count_letter.get(sym) >= count_letter:
                    list_true.append(True)
                else:
                    list_true.append(False)

            if all(list_true):
                result_words.append(word)

    result_words.sort(key=lambda item: (len(item), item))

    dict_len_and_word = dict()
    for word in result_words:
        val = dict_len_and_word.get(len(word))
        if val:
            val.append(word)
            dict_len_and_word[len(word)] = val
        dict_len_and_word.setdefault(len(word), [word])
    return dict_len_and_word
