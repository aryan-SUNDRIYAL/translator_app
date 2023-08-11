

from translate import Translator
from englisttohindi.englisttohindi import EngtoHindi
while(True):
    lang1= input("enter the source language : ")
    lang2= input("eneter the language in which you want to translate : ")
    message = input("enter the message that you want to translate: ")
    if(lang2=='hindi' or lang2 == 'HINDI' or lang2 == 'Hindi'):
        res = EngtoHindi(message)
        print(res.convert)
    else:    
        translator= Translator(from_lang=lang1,to_lang=lang2)
        translation = translator.translate(message)
        print(translation)
