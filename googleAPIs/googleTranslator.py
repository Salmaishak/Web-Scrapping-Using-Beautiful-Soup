from googletrans import Translator
#A Translator code

translator = Translator()
def translation(string):
    translation = translator.translate(string, dest='ar')
    return translation.text
