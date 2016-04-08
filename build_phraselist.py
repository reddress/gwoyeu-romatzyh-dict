import re

class HanPhrase:
    hanziList=[]
    pinyinList=[]
    hanziStr=""
    pinyinExactStr=""
    pinyinFuzzyStr=""
    definition=""

in_cedict=open('cedict','r',encoding='utf8')

# list of HanPhrase
HanPhraseList=[]

for line in in_cedict:
    tmpHanPhrase=HanPhrase()

    # set Hanzi string
    tmpHanziStr=line.split(" ",1)[0]
    tmpHanPhrase.hanziStr=tmpHanziStr
    
    tmpHanziList=[]
    
    # build ucp list
    for char in tmpHanziStr:
        tmpHanziList.append("U+" + hex(ord(char[0]))[2:].upper())

    tmpHanPhrase.hanziList=tmpHanziList

    # get pinyin exact string
    exactStr=re.findall('\[.*?\]',line)[0].strip("[]")
    tmpHanPhrase.pinyinExactStr=exactStr

    # set pinyin list
    tmpHanPhrase.pinyinList=exactStr.split()

    # set pinyin fuzzy string
    tmpHanPhrase.pinyinFuzzyStr=re.sub("[1-5]", "", exactStr)

    # set definition
    tmpHanPhrase.definition=re.findall('\/.*\/',line)[0]

    HanPhraseList.append(tmpHanPhrase)
