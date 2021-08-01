from translate import Translator

translator = Translator(to_lang="ja")

try:
    with open("./app/sad.txt", mode="r") as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
        with open("./app/yo.txt", mode="w") as my_file2:
            my_file2.write(translation)
except FileNotFoundError as err:
    print("file not found")