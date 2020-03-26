import json
from view import view
# coding: utf8
languages = {'afar': 'aa', 'abkhazian': 'ab', 'afrikaans': 'af', 'akan': 'ak', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'aragonese': 'an', 'armenian': 'hy', 'assamese': 'as', 'avaric': 'av', 'avestan': 'ae', 'aymara': 'ay', 'azerbaijani': 'az', 'bashkir': 'ba', 'bambara': 'bm', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bihari languages': 'bh', 'bislama': 'bi', 'tibetan': 'bo', 'bosnian': 'bs', 'breton': 'br', 'bulgarian': 'bg', 'burmese': 'my', 'catalan': 'ca', 'czech': 'cs', 'chamorro': 'ch', 'chechen': 'ce', 'chinese': 'zh', 'church slavic': 'cu', 'chuvash': 'cv', 'cornish': 'kw', 'corsican': 'co', 'cree': 'cr', 'welsh': 'cy', 'danish': 'da', 'german': 'de', 'maldivian': 'dv', 'dutch': 'nl', 'dzongkha': 'dz', 'greek': 'el', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'ewe': 'ee', 'faroese': 'fo', 'persian': 'fa', 'fijian': 'fj', 'finnish': 'fi', 'french': 'fr', 'western frisian': 'fy', 'fulah': 'ff', 'georgian': 'ka', 'gaelic; scottish gaelic': 'gd', 'irish': 'ga', 'galician': 'gl', 'manx': 'gv', 'guarani': 'gn', 'gujarati': 'gu', 'haitian': 'ht', 'hausa': 'ha', 'hebrew': 'he', 'herero': 'hz', 'hindi': 'hi', 'hiri motu': 'ho', 'croatian': 'hr', 'hungarian': 'hu', 'igbo': 'ig', 'icelandic': 'is', 'ido': 'io', 'sichuan yi': 'ii', 'inuktitut': 'iu', 'interlingue': 'ie', 'interlingua': 'ia', 'indonesian': 'id', 'inupiaq': 'ik', 'italian': 'it', 'javanese': 'jv', 'japanese': 'ja', 'kalaallisut': 'kl', 'kannada': 'kn', 'kashmiri': 'ks', 'kanuri': 'kr', 'kazakh': 'kk', 'central khmer': 'km', 'gikuyu': 'ki', 'kinyarwanda': 'rw', 'kyrgyz': 'ky', 'komi': 'kv', 'kongo': 'kg', 'korean': 'ko', 'kuanyama': 'kj', 'kurdish': 'ku', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'limburgan': 'li', 'lingala': 'ln', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'luba-katanga': 'lu', 'ganda': 'lg', 'macedonian': 'mk', 'marshallese': 'mh', 'malayalam': 'ml', 'maori': 'mi', 'marathi': 'mr', 'malay': 'ms', 'micmac': 'Mi', 'malagasy': 'mg', 'maltese': 'mt', 'mongolian': 'mn', 'nauru': 'na', 'navajo': 'nv', 'south ndebele': 'nr', 'north ndebele': 'nd', 'ndonga': 'ng', 'nepali': 'ne', 'dutch; flemish': 'nl', 'norwegian nynorsk': 'nn', 'norwegian bokmål': 'nb', 'norwegian': 'no', 'occitan': 'oc', 'ojibwa': 'oj', 'oriya': 'or', 'oromo': 'om', 'ossetic': 'os', 'punjabi': 'pa', 'pali': 'pi', 'polish': 'pl', 'portuguese': 'pt', 'pashto': 'ps', 'quechua': 'qu', 'romansh': 'rm', 'romanian': 'ro', 'rundi': 'rn', 'russian': 'ru', 'sango': 'sg', 'sanskrit': 'sa', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'northern sami': 'se', 'samoan': 'sm', 'shona': 'sn', 'sindhi': 'sd', 'somali': 'so', 'sotho': 'st', 'spanish': 'es', 'sardinian': 'sc', 'serbian': 'sr', 'swati': 'ss', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tahitian': 'ty', 'tamil': 'ta', 'tatar': 'tt', 'telugu': 'te', 'tajik': 'tg', 'tagalog': 'tl', 'thai': 'th', 'tigrinya': 'ti', 'tonga': 'to', 'tswana': 'tn', 'tsonga': 'ts', 'turkmen': 'tk', 'turkish': 'tr', 'twi': 'tw', 'uyghur': 'ug', 'ukrainian': 'uk', 'urdu': 'ur', 'uzbek': 'uz', 'venda': 've', 'vietnamese': 'vi', 'volapük': 'vo', 'walloon': 'wa', 'wolof': 'wo', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zhuang': 'za', 'zulu': 'zu'}
def getLang():
    lang = input("Subtitle Language : ").lower()
    if lang in languages:
        lang = languages[lang]
    else:
        print('Language Not Found.... Exiting')
        exit()
    return lang

def getData():
    query = []
    while True:
        t = input("Movie Or TV Series (T for TV Series or M for Movie ) : ")
        if t.lower() == 'm' or t.lower() == 't':
            break
        else:
            print("Enter proper input")
            pass
    name = ""
    lang = ""
    season = ""
    episode = ""
    if t.lower() == 'm':
        name = input("Movie Name : ")
        lang = getLang()
        obj = view(name,lang).genJSONtype()
        query.append(obj)
        return query
    else:
        while True:
            ch = input("1 for Single Episode \n2 for Single Season\n3 for Entire Series\n4 for Multiple Episodes\n5 to Quit\nEnter Your Choice : ")
            if ch in [str(i) for i in range(1,5)]:
                break
            else:
                print("Enter Proper Input ")
        ch = int(ch)
        if ch == 1:
            name = input("Series Name : ")
            season = input('Season # : ')
            episode = input('Episode # : ')
            lang = getLang()
            obj = view(name,lang,season,episode).genJSONtype()
            l = []
            l.append(obj)
            return l
        elif ch == 2:
            name = input("Series Name : ")
            season = input('Season # : ')
            ep = input("# of episodes per season : ")
            lang = getLang()
            t = []
            for x in range(1,int(ep)+1):
                t.append(view(name,lang,season,x).genJSONtype())
            return t
        elif ch == 3:
            name = input("Series Name : ")
            ses = input("# of Seasons ")
            ep = input("# of episodes per season : ")
            lang = getLang()
            t = []
            for x in range(1,int(ses)+1):
                for y in range(1,int(ep)+1):
                    t.append(view(name,lang,x,y).genJSONtype())
            return t
        elif ch == 4:
            name = input("Series Name : ")
            lang = getLang()
            if lang in languages:
                lang = languages[lang]
            eps = []
            flag = True
            print("Enter Episodes................\n")
            while flag:
                season = input('Season # : ')
                episode = input('Episode # : ')
                ch = input("Press y to continue : ")
                eps.append(view(name,lang,season,episode).genJSONtype())

                flag = True if ch.lower() == 'y' else False
                if not flag:
                    print('Exiting..........')
                    break
            return eps
        elif ch == 5:
            print("Quiting")
    print("Done")


def genJSONFromData(data):
    with open('./tmp.json','w') as f:
        json.dump(data,f)


