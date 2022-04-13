from requests import get as _get


def translate(text, tl='en', sl='auto', raw=False):
    if type(text) is str:
        url = 'https://translate.googleapis.com/translate_a/single?client=gtx&sl='+sl+'&tl='+tl+'&dt=t&q='+text
        ret = _get(url=url).json()
        if not raw:
            _ret = ''
            for i in ret[0]:
                _ret += i[0]
            ret = _ret
    elif type(text) is dict:
        ret = {}
        for i in text:
            ret[i] = translate(text[i], tl, sl, raw)
    elif type(text) is list:
        ret = []
        for i in text:
            ret.append(translate(i, tl, sl, raw))
    else:
        ret = None
    return ret

def check_lang(text):
    if type(text) is str:
        url = 'https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl=en&dt=t&q='+text
        ret = _get(url=url).json()
        ret = ret[2]
    elif type(text) is dict:
        ret = {}
        for i in text:
            ret[i] = check_lang(text[i])
    elif type(text) is list:
        ret = []
        for i in text:
            ret.append(check_lang(i))
    else:
        ret = None
    return ret


langs = {'Afrikaans': 'af', 'Albanisch': 'sq', 'Amharisch': 'am', 'Arabisch': 'ar', 'Armenisch': 'hy', 'Aserbaidschanisch': 'az', 'Baskisch': 'eu', 'Weißrussisch': 'be', 'Bengalisch': 'bn', 'Bosnisch': 'bs', 'Bulgarisch': 'bg', 'Katalanisch': 'ca', 'Cebuano': 'ceb', '(vereinfacht)': 'zh-CN', '(traditionell)': 'zh-TW', 'Korsisch': 'co', 'Kroatisch': 'hr', 'Tschechisch': 'cs', 'Dänisch': 'da', 'Niederländisch': 'nl', 'Englisch': 'en', 'Esperanto': 'eo', 'Estnisch': 'et', 'Finnisch': 'fi', 'Französisch': 'fr', 'Friesisch': 'fy', 'Galicisch': 'gl', 'Georgisch': 'ka', 'Deutsch': 'de', 'Griechisch': 'el', 'Gujarati': 'gu', '(Haiti)': 'ht', 'Haussa': 'ha', 'Hawaiianisch': 'haw', 'Hebräisch': 'he', 'Hindi': 'hi', 'Hmong': 'hmn', 'Ungarisch': 'hu', 'Isländisch': 'is', 'Igbo': 'ig', 'Indonesisch': 'id', 'Irisch': 'ga', 'Italienisch': 'it', 'Japanisch': 'ja', 'Javanisch': 'jv', 'Kannada': 'kn', 'Kasachisch': 'kk', 'Khmer': 'km', 'Kinyarwanda': 'rw', 'Koreanisch': 'ko', 'Kurdisch': 'ku', 'Kirgisisch': 'ky', 'Lao': 'lo', 'Latein': 'la', 'Lettisch': 'lv', 'Litauisch': 'lt', 'Luxemburgisch': 'lb', 'Mazedonisch': 'mk', 'Madagạssisch': 'mg', 'Malaiisch': 'ms', 'Malayalam': 'ml', 'Maltesisch': 'mt', 'Maori': 'mi', 'Marathi': 'mr', 'Mongolisch': 'mn', '(Birmanisch)': 'my', 'Nepalesisch': 'ne', 'Norwegisch': 'no', '(Chichewa)': 'ny', '(Oriya)': 'or', 'Paschtunisch': 'ps', 'Persisch': 'fa', 'Polnisch': 'pl', 'Brasilien)': 'pt', 'Pandschabi': 'pa', 'Rumänisch': 'ro', 'Russisch': 'ru', 'Samoanisch': 'sm', 'Gälisch': 'gd', 'Serbisch': 'sr', 'Sesotho': 'st', 'Shona': 'sn', 'Sindhi': 'sd', 'Singhalesisch': 'si', 'Slowakisch': 'sk', 'Slowenisch': 'sl', 'Somali': 'so', 'Spanisch': 'es', 'Sundanesisch': 'su', 'Swahili': 'sw', 'Schwedisch': 'sv', '(Philippinisch)': 'tl', 'Tadschikisch': 'tg', 'Tamil': 'ta', 'Tatarisch': 'tt', 'Telugu': 'te', 'Thai': 'th', 'Türkisch': 'tr', 'Turkmenisch': 'tk', 'Ukrainisch': 'uk', 'Urdu': 'ur', 'Uigurisch': 'ug', 'Usbekisch': 'uz', 'Vietnamesisch': 'vi', 'Walisisch': 'cy', 'Xhosa': 'xh', 'Jiddisch': 'yi', 'Yoruba': 'yo', 'Zulu': 'zu'}
