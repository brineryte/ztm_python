from translate import Translator

translator = Translator(to_lang="ja")

with open('../text_files/heythere.txt', mode='r') as file:
    text = file.read()
    translation = translator.translate(text)
    with open('../text_files/translated.txt', mode='w', encoding="utf-8") as translated_file:
        translated_file.write(translation)
