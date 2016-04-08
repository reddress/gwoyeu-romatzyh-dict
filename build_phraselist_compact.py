import re
import fnmatch

class HanPhrase:
    hanziStr=""
    pinyinExactStr=""
    definition=""

in_cedict=open('cedict','r',encoding='utf8')

# list of HanPhrase
HanPhraseList=[]

for line in in_cedict:
#    if not fnmatch.fnmatch(line,"*(idiom)*"):
        
        tmpHanPhrase=HanPhrase()

        # set Hanzi string
        tmpHanziStr=line.split(" ",1)[0]
        tmpHanPhrase.hanziStr=tmpHanziStr
        
        # get pinyin exact string
        exactStr=re.findall('\[.*?\]',line)[0].strip("[]")
        tmpHanPhrase.pinyinExactStr=exactStr

        # set definition
        tmpHanPhrase.definition=re.findall('\/.*\/',line)[0]

        HanPhraseList.append(tmpHanPhrase)
