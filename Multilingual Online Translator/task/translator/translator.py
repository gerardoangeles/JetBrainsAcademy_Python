import sys
import os
import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup

languages_dict = {
    0: "All",
    1: "Arabic",
    2: "German",
    3: "English",
    4: "Spanish",
    5: "French",
    6: "Hebrew",
    7: "Japanese",
    8: "Dutch",
    9: "Polish",
    10: "Portuguese",
    11: "Romanian",
    12: "Russian",
    13: "Turkish"
}


class Translator:

    def __init__(self):
        self.lang_from = None
        self.lang_to = None
        self.text = None
        self.translations_lst = list()
        self.examples_lst = list()
        self.url = ""
        self.translate_to = ""
        self.soup = None
        self.language = None
        self.available_lang_dic = languages_dict
        self.language_number_from = 0
        self.language_number_to = 0

    def config_translate(self):
        self.url = "https://context.reverso.net/translation/"
        # from ▶ to
        self.language = self.available_lang_dic[self.language_number_to]
        languages = f"{self.available_lang_dic[self.language_number_from].lower()}-{self.available_lang_dic[self.language_number_to].lower()}/"
        self.url = self.url + languages
        self.url = self.url + self.text

    def set_soup(self):
        user_agent = 'Mozilla/5.0'
        try:
            response = requests.get(self.url, headers={'User-Agent': user_agent})
            response.raise_for_status()
        except HTTPError as http_err:
            # HTTP error occurred: 404 Client Error: Not Found for url:
            print(f"Sorry, unable to find {self.text}")
            sys.exit()
        except Exception as err:
            print("Something wrong with your internet connection")  # Python 3.6
            sys.exit()
        else:
            if response.status_code != requests.codes.ok:  # 200
                print("?", response.status_code)
                if response.status_code == 404:
                    # HTTP error occurred: 404 Client Error: Not Found for url:
                    print(f"Sorry, unable to find {self.text}")
                else:
                    print("Something wrong with your internet connection")
                sys.exit()
            self.soup = BeautifulSoup(response.content, 'html.parser')

    def set_translations(self, times):
        self.translations_lst = []
        translations_content = self.soup.select("#translations-content .translation")
        for translation in translations_content:
            self.translations_lst.append(translation.get_text().strip())
            if times == 1:
                break

    def set_example(self, times):
        self.examples_lst = []
        examples_content = self.soup.select("#examples-content .example .text")
        for i, example in enumerate(examples_content):
            self.examples_lst.append(example.get_text().strip())
            if times == 1 and i == 1:
                break

    def show_translations(self):
        print(f"{self.language} Translations:")
        print(*self.translations_lst, sep='\n', end="")

    def show_examples(self):
        print(f"{self.language} Examples:")
        for i, e in enumerate(self.examples_lst):
            if i != 0 and i % 2 == 0:
                print()
            print(e)

    def save_translations(self):
        file_name = self.text + ".txt"
        if os.path.exists(file_name):
            with open(file_name, "a", encoding='utf-8') as file:
                file.write(f"{self.language} Translations:\n")
                for translation in self.translations_lst:
                    file.write(str(translation) + "\n\n")
        else:
            print("WARN!")

    def save_examples(self):
        file_name = self.text + ".txt"
        if os.path.exists(file_name):
            with open(file_name, "a", encoding='utf-8') as file:
                file.write(f"{self.language} Example:\n")
                for example in self.examples_lst:
                    file.write(str(example) + "\n")
                file.write("\n")
        else:
            print("WARN!")

    def show_saved_file(self):
        file_name = self.text + ".txt"
        with open(file_name, 'r') as result:
            print(result.read())


def start(test):
    print('Hello, welcome to the translator. Translator supports:')
    for k, v in languages_dict.items():
        if k != 0:
            print(f"{k}. {v}")

    print("Type the number of your language:")

    if test:
        number_lang_from = 3
        print(number_lang_from)
        print("Type the number of a language you want to translate to or '0' to translate to all languages:")
        number_lang_to = 0
        print(number_lang_to)
        print('Type the word you want to translate:')
        word = "hello"
        print(word)
    else:
        number_lang_from = int(input())
        print("Type the number of language you want to translate to:")
        number_lang_to = int(input())
        print('Type the word you want to translate:')
        word = input()

    return {"from": number_lang_from, "to": number_lang_to, "word": word}


def generic(t):
    t.set_soup()
    t.set_translations(1)
    t.set_example(1)
    t.save_translations()
    t.save_examples()
    t.show_saved_file()


def convert_to_number(translate_dict):
    # python translator.py english french hello
    for k_t, v_t in languages_dict.items():
        if v_t.lower() == translate_dict["source_language"]:
            translate_dict["source_language"] = k_t
        if v_t.lower() == translate_dict["target_language"]:
            translate_dict["target_language"] = k_t

    if translate_dict["target_language"] == "all":
        translate_dict["target_language"] == 0

    return translate_dict


def validate_input():
    prg_name, src_lang, tg_lang, third_arg = "", "", "", ""
    if len(sys.argv) >= 1:
        prg_name = sys.argv[0]
    if len(sys.argv) >= 2:
        src_lang = sys.argv[1]
    if len(sys.argv) >= 3:
        tg_lang = sys.argv[2]
    if len(sys.argv) >= 4:
        third_arg = sys.argv[3]
    if src_lang != "" and tg_lang != "":
        return {"source_language": src_lang, "target_language": tg_lang, "word": third_arg}
    return {}


def validate_language(l_from, l_to):
    # Sorry, the program doesn't support korean
    langs = [l.lower() for l in languages_dict.values()]
    if l_from.lower() not in langs:
        print(f"Sorry, the program doesn't support {l_from}")
        sys.exit()
    if l_to.lower() not in langs:
        print(f"Sorry, the program doesn't support {l_to}")
        sys.exit()


def cli():
    translate = validate_input()
    validate_language(translate["source_language"], translate["target_language"])

    if translate != {}:
        translator = Translator()
        translate = convert_to_number(translate)
        translator.language_number_from = translate["source_language"]
        translator.language_number_to = translate["target_language"]
        translator.text = translate["word"]
        open(translator.text + ".txt", 'w', encoding='utf-8').close()
        translator.config_translate()

        if translator.language_number_to == 0:
            for k_2, _ in languages_dict.items():
                if k_2 != 0:
                    translator.language_number_to = k_2
                    translator.config_translate()
                    generic(translator)
        else:
            generic(translator)


if __name__ == '__main__':
    cli()
