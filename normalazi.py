import re

CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ'
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")

TRANS = dict()

for cyrllic, latin in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(cyrllic)] = latin
    TRANS[ord(cyrllic.upper())] = latin.upper()


def normalize(name: str) -> str:
    translate_name = re.sub(r'[^a-zA-Z0-9_\.]', '_', name.translate(TRANS))
    return translate_name



#print(normalize('ывалырв#$а1(23).jpg'))