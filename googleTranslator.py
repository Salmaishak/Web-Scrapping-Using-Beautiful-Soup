from googletrans import Translator

translator = Translator()
translation = translator.translate("life", dest='ar')
print(translation.text)
