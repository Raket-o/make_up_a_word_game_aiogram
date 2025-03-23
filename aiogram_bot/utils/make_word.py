"""The word search module."""

import pathlib


class FindWords:
    def __init__(self, file_name:str) -> None:
        self.file_name = file_name
        self.dict_words = []

    def update_dict_words(self) -> None:
        """
        The update_dict_words function opens a file with the words
        and stores the list in self.dict_words.
        """
        path_file = pathlib.Path(__file__).parent.resolve()
        with open(path_file.joinpath(self.file_name), "r", encoding="utf-8") as file:
            self.dict_words = file.read().lower().split()

    async def get_find_words(self, user_word: str) -> dict[int:list[str]]:
        """
        The get_find_words function.
        Finds all the words that can be composed from user_word.
        Returns a dictionary with a nested list of {number of letters: [words]}.
        """
        user_word_split = list(user_word)
        for ind, sym in enumerate(user_word):
            if ord(sym) == 235:
                user_word_split[ind] = "ё"

        user_word = "".join(user_word_split)
        result_words = []
        dict_count_letter = {sym: user_word.count(sym) for sym in user_word}
        for word in self.dict_words:
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


find_words_obj = FindWords("russian_nouns.txt")
find_words_obj.update_dict_words()
